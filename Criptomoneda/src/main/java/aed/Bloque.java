package aed;

import java.util.ArrayList;

public class Bloque {


    private Heap<Transaccion> txPorMonto;
    private ArrayList<Transaccion> txPorId;
    private int sumaMontosSinCreacion;
    private int cantidadTxSinCreacion;

    /*
     *      Heap<Transaccion> txPorMonto:
     *              Heapmax de transacciones para acceder en O(1) a la mayor y
     *              para extraerla en O(log nb)
     *      ArrayList<Transaccion>  txPorId:
     *              Lista de transacciones por id para devolver copia en O(nb)
     *      int sumaMontosSinCreacion
     *      int cantidadTxSinCreacion       Estos dos para calcular en O(1) el promedio.
     * */

    public Bloque(Transaccion[] tx){
        this.txPorId = new ArrayList<Transaccion>();                //O(1)
        for (Transaccion t : tx) {
            this.txPorId.add(t.copy());                                    // nb * O(1) = O(nb)
        }
        // Se crea el heap
        this.txPorMonto = new Heap<Transaccion>(this.txPorId);

        for (int i = 0 ; i< tx.length ; i++){
            Transaccion t = tx[i];
            if (!t.esCreacion()) {
                sumaMontosSinCreacion += t.monto();
                cantidadTxSinCreacion++;
            }
        }
    }
    public Heap<Transaccion> getTxPorMonto() {
        return txPorMonto;
    }

    public ArrayList<Transaccion> getTxPorId(){
        ArrayList<Transaccion> transacciones = new ArrayList<>();
        for (Transaccion transaccion : txPorId){
            if (transaccion.monto()>=0){
                transacciones.add(transaccion);
            }
        }
        return transacciones;
    }

    public int getSumaMontosSinCreacion() {
        return sumaMontosSinCreacion;
    }

    public int getCantidadTxSinCreacion() {
        return cantidadTxSinCreacion;
    }

    public void hackearBloque(Transaccion transaccion){

        int idComprador = transaccion.id_comprador();
        int monto = transaccion.monto();

        if (idComprador != 0){
            cantidadTxSinCreacion-=1;
            sumaMontosSinCreacion-= monto;

        }
        int posicion = transaccion.getId();
        Transaccion hackeada = new Transaccion(posicion,-1,-1,-1);
        this.txPorId.set(posicion,hackeada);
    }
}
