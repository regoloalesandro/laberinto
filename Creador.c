#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
void inicializarLab(int dimension,char** laberinto,int obstaculosRand){
    int indice = 0;
    char fila[dimension];
    if(obstaculosRand<((dimension*dimension)/2)){
        for(indice = 0; indice < dimension; indice++){
            fila[indice] = '0' ;
        }
        fila[indice] = '\0';
        for(indice = 0; indice < dimension; indice++){
            strcpy(laberinto[indice],fila);
        }  
    }
    else{  
        for(indice = 0; indice < dimension; indice++){
            fila[indice] = '1' ;
        }
        fila[indice+1] = '\0';
        for(indice = 0; indice < dimension; indice++){
            strcpy(laberinto[indice],fila);
        }
    }
}
void generadorDeObstaculos(int dimension,char** laberinto,int obstaculosRand){
    int indice = 0, fila = 0, columna =0;
    while(indice<obstaculosRand){
        fila = rand() % (dimension);
        columna = rand() % (dimension);
        if(obstaculosRand<((dimension*dimension)/2)){
            if(laberinto[fila][columna] == '0' ){
                laberinto[fila][columna] = '1';
                indice ++;
            }
        }
        else{
            if(laberinto[fila][columna]== '1'){
                laberinto[fila][columna] = '0';
                indice ++;
            }
        }
    }
}

// Lee los parametros ingresados en el archivo y crea una matriz que representa el laberinto
char** CreacionDelLab(FILE *Entrada,char** laberinto){
    int dimension , fila, columna,obstaculosRand, indice = 0,flag = 0,posIx,posIy,posXx,posXy;
    char Basura[1024]; 
    fscanf(Entrada,"%[^\n]\n",Basura);
    fscanf(Entrada,"%d\n",&dimension);
    laberinto = (char**) malloc(sizeof(char*)*dimension);
    for(indice = 0; indice < dimension; indice++){

        laberinto[indice] = (char*) malloc(sizeof(char)*(dimension+1));
    }
    fscanf(Entrada,"%[^\n]\n",Basura);
    while(fgetc(Entrada) == '(' && flag == 0){

        fscanf(Entrada,"%d,%d)\n",&fila,&columna);
        if(!(fila<dimension && fila > 0 && columna<dimension && columna > 0) )
        {
            flag++;
        }
        
    }
    if(flag == 0){
        fscanf(Entrada,"%[^\n]\n",Basura);
        fscanf(Entrada,"%d \n",&obstaculosRand);
        if(obstaculosRand < (dimension*dimension)){
            inicializarLab(dimension,laberinto,obstaculosRand);
            rewind(Entrada);
            fscanf(Entrada,"%[^\n]\n",Basura);
            fscanf(Entrada,"%d \n",&dimension);
            fscanf(Entrada,"%[^\n]\n",Basura);
            while(fgetc(Entrada) == '('){
                fscanf(Entrada,"%d,%d)\n",&fila,&columna);
                fila --;
                columna --;
                laberinto[fila][columna] = '1';
            }
            fscanf(Entrada,"%[^\n]\n",Basura);
            fscanf(Entrada,"%d\n",&obstaculosRand);
            fscanf(Entrada,"%[^\n]\n",Basura);
            fscanf(Entrada,"(%d,%d)\n",&posIy,&posIx);
            if(posIy<(dimension + 1) && posIy > 0 && posIx<(dimension + 1) && posIx > 0){
            posIy --;
            posIx --;
            laberinto[posIy][posIx] = 'I';
            }
            fscanf(Entrada,"%[^\n]\n",Basura);
            fscanf(Entrada,"(%d,%d)",&posXy,&posXx);
            if(posXy<(dimension + 1) && posXy > 0 && posXx<(dimension + 1) && posXx > 0 && posXx != posIx && posIy != posXy ){
            posXy --;
            posXx --;
            laberinto[posXy][posXx] = 'X';
            generadorDeObstaculos(dimension,laberinto,obstaculosRand);
            }
        }
    }
        return laberinto;
}
int main(int argc, char *argv[]){
    char Basura[1024];
    FILE *Entrada,*Salida;
    char **Lab = NULL;
    int dimension = 0,indice = 0;
    srand(time(NULL));
    Entrada = fopen(argv[1],"r");
    Lab = CreacionDelLab(Entrada,Lab);
    rewind(Entrada);
    fscanf(Entrada,"%[^\n]\n",Basura);
    fscanf(Entrada,"%d \n",&dimension);
    Salida = fopen("salida.txt","w+");
    for(indice = 0; indice < dimension; indice++){
        fprintf(Salida,"%s\n",Lab[indice]);
    }
    for(indice = 0; indice < dimension; indice++){
        free(Lab[indice]);
    }
    free(Lab);
    fclose(Salida);
   // printeoDeLab(Lab,dimension);
}


