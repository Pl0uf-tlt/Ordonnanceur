#include <stdio.h>
#include <stdlib.h>


typedef struct process
{
  char nom[20];
  int TpsExe;
  int TpsArr;
  int TpsFin;
  int TpsSej;
  int TpsAtt;
  int Prio;
} process;

void triTpsArr(process* proc , int nbp)
{int i,j;
  // Tri des processus en fonction tu TpsArr (Temps Arriv�e)
  process reserve;
  for (i = 0; i<nbp; i++)
  {
    for (j = 1; j<(nbp-i); j++)
    {
      if (proc[j-1].TpsArr > proc[j].TpsArr)
      {
        reserve = proc[j-1];
        proc[j-1] = proc[j];
        proc[j] = reserve;
      }
    }
  }

  // Afficher l'enchainement des processus
  for(i=0;i<nbp;i++)
  { for(j=0;j<proc[i].TpsExe;j++)
    { printf("%s ",proc[i].nom);
    }
  }
  printf("\n\n");
}

void triPrio(process* proc,int nbp, int tps, process** proc_prio, int nbPrio) {
    triTpsArr(proc, nbp);
    
}
int main() {
    int nbp = 8;
    process* proc;
    proc=(process *)malloc(sizeof(process)*nbp);
    strcpy(proc[0].nom,"P1");
    proc[0].TpsExe=6;
    proc[0].Prio=2;
    proc[0].TpsArr=0;
    strcpy(proc[1].nom,"P2");
    proc[1].TpsExe=2;
    proc[1].Prio=4;
    proc[1].TpsArr=2;
    strcpy(proc[2].nom,"P3");
    proc[2].TpsExe=1;
    proc[2].Prio=0;
    proc[2].TpsArr=7;
    strcpy(proc[3].nom,"P4");
    proc[3].TpsExe=5;
    proc[3].Prio=0;
    proc[3].TpsArr=0;
    strcpy(proc[4].nom,"P5");
    proc[4].TpsExe=4;
    proc[4].Prio=5;
    proc[4].TpsArr=11;
    strcpy(proc[5].nom,"P6");
    proc[5].TpsExe=4;
    proc[5].Prio=1;
    proc[5].TpsArr=13;
    strcpy(proc[6].nom,"P7");
    proc[6].TpsExe=1;
    proc[6].Prio=3;
    proc[6].TpsArr=4;
    strcpy(proc[7].nom,"P8");
    proc[7].TpsExe=3;
    proc[7].Prio=1;
    proc[7].TpsArr=8;
}