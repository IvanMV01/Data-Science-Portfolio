package aed;

public interface Priorizable<T> extends Comparable<T>{

    /*
     * Se creó esta interfaz porque el Heap requería hacer operaciones sobre la variable T que
     * puede ser tanto un usuario como una transacción.
     */
    void setHandle(HeapHandle<T> h);
    HeapHandle<T> getHandle();
    T copy();
}
