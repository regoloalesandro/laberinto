#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

/*
    El buffer de los string a la hora de leer los parametros sera de 1024, por lo que
    palabras largas generaran un error en el funcionamiento del programa 
*/
#define buff  1024

/*
    inicializaLab toma un entero que representa el tamaño del laberinto, un puntero a puntero de char ques es
    una refernecia a donde se alamecenara el laberinto y la cantidad de obstaculos randoms
    Dependiendo de la cantidad de obstaculos randoms que tengo el laberinto se inicializa de forma distinta
    Si la cantidad de randoms es mayor a la mintad de los espacios posibles, el laberinto se inicializa con 
    todos 1  
    En caso contrario se inicializa el laberinto con todos 0
    */
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
/*
    generadorDeObstaculos toma un entero que representa el largo del laberinto, un puntero a puntero de char
    que es la referencia de a donde se guarda el laberinto y la cantidad de obstaculos randoms.
    La funcion se fija la cantidad si la cantidad de randoms es mayor a la mintad de los espacios posibles, los randoms 
    a generar representaran los espacios donde se puede pasar. En cao contrario los randoms representaran las paredes 
*/
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
/*
 CreacionDelLab toma el un puntero al archivo de entradam un puntero a puntero de char que indica donde
 se alamacenara el laberinto y un puntero a entero que sirvira com bandera para ver si la funcion
 fue exitosa o no.
 Lee los parametros ingresados en el archivo y crea una matriz que representa el laberinto
*/
char** CreacionDelLab(FILE *Entrada,char** laberinto,int *success){
    int dimension , fila, columna,obstaculosRand, indice = 0,flag = 0,posIx,posIy,posXx,posXy;
    char Basura[ buff ]; 
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
            success[0] = 1;
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
            else
            {
                success[0] = 1;
            }
            fscanf(Entrada,"%[^\n]\n",Basura);
            fscanf(Entrada,"(%d,%d)",&posXy,&posXx);
            if(posXy<(dimension + 1) && posXy > 0 && posXx<(dimension + 1) && posXx > 0 && posXx != posIx && posIy != posXy ){
            posXy --;
            posXx --;
            laberinto[posXy][posXx] = 'X';
            generadorDeObstaculos(dimension,laberinto,obstaculosRand);
            }
             else
            {
                success[0] = 1;
            }
        }
    }
        return laberinto;
}
int main(int argc, char *argv[]){
    char Basura[buff];
    FILE *Entrada,*Salida;
    char **Lab = NULL;
    int success = 0; 
    int dimension = 0,indice = 0;
    srand(time(NULL));
    Entrada = fopen(argv[1],"r");
    Lab = CreacionDelLab(Entrada,Lab,&success);
    if(success==0){
    rewind(Entrada);
    fscanf(Entrada,"%[^\n]\n",Basura);
    fscanf(Entrada,"%d \n",&dimension);
    Salida = fopen(argv[2],"w+");
    for(indice = 0; indice < dimension; indice++){
        fprintf(Salida,"%s\n",Lab[indice]);
    }
    for(indice = 0; indice < dimension; indice++){
        free(Lab[indice]);
    }
    }
    free(Lab);
    fclose(Salida);
   return success;
}


