package aed;
import java.lang.reflect.Array;
import java.util.ArrayList;


public class Heap<T extends Priorizable<T>> {
    private ArrayList<T> datos;

    /*
    *  Se implementa el Heap-max sobre un ArrayList, porque maneja la memoria
    * de forma óptima. Esto es: cuando el array se llena, se crea un nuevo array
    * del doble de tamaño. Esto es exáctamente el espacio que necesita el heap
    * para el próximo nivel.
    *  */

    public Heap(){
        this.datos = new ArrayList<T>();                        //O(1)
    }

    public Heap(ArrayList<T> tLista){
        datos = new ArrayList<T>(tLista);                           //O(1)
        for (int i = 0; i < datos.size(); i++) {                    //O(n)
            HeapHandle<T> h = new HeapHandle<>(i, datos.get(i));
            datos.get(i).setHandle(h);
        }
        int ultimoNoHoja = datos.size()/2 -1;           // O(n)  (algoritmo de Floyd)
        for (int i = ultimoNoHoja ; i >= 0; i--) {
            siftDown(i);
        }
    }

    public Heap(T[] arreglo){

        /*
            Igual que el anterior, pero toma como parámetro un arreglo,
            que es copiado a un ArrayList para luego usar el algoritmo
            de Floyd.
        * */

        datos = new ArrayList<T>();
        for (int i = 0; i < arreglo.length; i++) {
            datos.add(arreglo[i]);
        }

        // handles
        for (int i = 0; i < datos.size(); i++) {
            HeapHandle<T> h = new HeapHandle<>(i, datos.get(i));
            datos.get(i).setHandle(h);
        }
        int ultimoNoHoja = datos.size()/2 -1;
        // heapify  (floyd otra vez)
        for (int i = ultimoNoHoja; i >= 0; i--) {
            siftDown(i);
        }

    }

    public HeapHandle<T> insertar (T elem){
        // inserta elemento al final, hace siftUp y devuelve  handle.
        int posicion = datos.size();
        HeapHandle<T> handle = new HeapHandle<T>(posicion,elem);
        this.datos.add(elem);
        siftUp(posicion);
        return handle;
    }

    public T max(){
        //devuelve el maximo
        if (this.datos.size() == 0 ) return null;
        return this.datos.get(0);
    }

    public T extraerMax(){
        // extrae el maximo en O(log n)

        if (datos.isEmpty()) return null;           //O(1)
        T maximo = datos.get(0);                    //O(1)

        int ultimo_indice = datos.size()-1;         //O(1)
        this.swap(0,ultimo_indice);               //O(1)

        this.datos.remove(ultimo_indice);           //O(1) (por ser el último)
        if(!datos.isEmpty()){
            siftDown(0);                          //O(log n)
        }
        maximo.setHandle(null);                      //O(1)
        return maximo.copy();                        //O(1)
    }
    public void eliminar(T elem){
        int ultimo_indice = datos.size()-1;
        int pos_elem = elem.getHandle().posicion;
        this.swap(pos_elem,ultimo_indice);
        this.datos.remove(ultimo_indice);
        if(!datos.isEmpty()){
            siftDown(pos_elem);
        }
    }

    private void swap(int i, int j){
        // intercambia la posicion de dos elementos y actualiza sus handles.
        T primero = this.datos.get(i);
        T segundo = this.datos.get(j);

        this.datos.set(i,segundo);
        this.datos.set(j, primero);

        HeapHandle<T> hprimero = primero.getHandle();
        HeapHandle<T> hsegundo = segundo.getHandle();

        if (hprimero != null) hprimero.posicion = j;
        if (hsegundo != null) hsegundo.posicion = i;
    }

    private int pos_padre(int i){
        return (i-1)/2;
    }

    private void siftUp(int i) {
        //Mientras sea mayor que el padre, intercambia. Los handles se actualizan dentro de swap.
        while (i > 0 && datos.get(i).compareTo(datos.get(pos_padre(i))) > 0) {
            int padre = pos_padre(i);
            swap(i, padre);
            i = padre;
        }
    }
    private void siftDown(int i){
        // mientras tenga hijos más grandes intercambia con el hijo mayor. En cada swap se actualizan handles.
        int izq = 2*i+1;
        int der = 2*i +2;
        int mayor = i;

        if (izq < this.datos.size() && this.datos.get(izq).compareTo(datos.get(mayor))>0 ){
            mayor = izq;
        }
        if (der< this.datos.size() && this.datos.get(der).compareTo(datos.get(mayor))>0){
            mayor = der;
        }
        if (mayor != i){
            swap (mayor, i);
            siftDown(mayor);
        }
    }
    public void update(HeapHandle<T> elem){
        // Actualiza la posicion del elemento en el heap  en O(log n)
        int i = elem.posicion;                                                          //O(1)
        if (i > 0 && datos.get(i).compareTo(datos.get(pos_padre(i))) > 0) {             //O(1)
            siftUp(i);                                                                  //O(log n)
        } else {
            siftDown(i);                                                                //O(log n)
        }

    }

    public  ArrayList<T>getData(){
        //Devuelve una copia del array del heap
        ArrayList<T> heapData= new ArrayList<T>();

        for ( int i=0 ; i< datos.size(); i++ ){
            heapData.add(datos.get(i));
        }
        return heapData;
    }

}
