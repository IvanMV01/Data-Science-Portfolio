package aed;

public class HeapHandle<T> {
    public int posicion;
    public T elemento;

    public HeapHandle(int posicion,  T elem){
        this.posicion = posicion ;
        this.elemento = elem;
    }
}
