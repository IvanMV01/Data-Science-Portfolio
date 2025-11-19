package aed;
import java.util.ArrayList;

public class Berretacoin {
    private Usuario[] usuarios;
    private Heap<Usuario> heapUsuarios;
    private ArrayList<Bloque> blockchain;

    /*
    *       Usuario[] usuarios:
    *                   Es un array de usuarios ordenados por id. Solo se usa para acceder
    *                   a un usuario en O(1) y modificar sus atributos si es necesario.
    *
    *      Heap<Usuario> heapUsuarios:
    *                   Es un heapmax de usuarios ordenados por saldo (menor id en caso de empate).
    *                   cada usuario tiene un handle que permite ubicar su posición en el árbol.
    *                   Con esta estructura se puede actualizar la posición de un usuario en O(log P)
    *                   y obtener el máximo en O(1).
    *
    *
    *      ArrayList<Bloque> blockchain:
    *                   Es una lista con todos los bloques. Se eligió esta estructura porque solo
    *                   se necesita acceso en O(1) y agregar bloque en O(1).
    *
    * */


    //***************************************************************************************
    public Berretacoin(int n_usuarios){

        // Debe hacerse en  O(P)


        this.usuarios = new Usuario[n_usuarios];                //O(1)

        //
        for (int i = 0; i<n_usuarios; i++){                     //O(P)
            usuarios[i]= new Usuario(i+1, 0);          //
        }
        this.heapUsuarios = new Heap<Usuario>(this.usuarios);   //O(P)
        this.blockchain = new ArrayList<Bloque>();              //O(1)
    }
    //****************************************************************************************
    public void agregarBloque(Transaccion[] transacciones){

        //Debe hacerse en O(nb*log p)

        for (Transaccion t : transacciones) {                   //para cada transaccion (nb)
            int monto = t.monto();           // O(1)

            if (!t.esCreacion()) {              // O(1)
                Usuario comprador = this.usuarios[t.id_comprador()-1];   //O(1)
                comprador.decrementarSaldo(monto);                          //O(1)
                this.heapUsuarios.update(comprador.getHandle());            //O(log(P))
            }
            Usuario vendedor = this.usuarios[t.id_vendedor()-1];         //O(1)
            vendedor.incremetarSaldo(monto);                                //O(1)
            this.heapUsuarios.update(vendedor.getHandle());                 //O(log(P))
        }

        //Hasta acá tenemos:   O(nb)*[5*O(1)+2*O(log P)] ) =  O(nb * log(P))


        Bloque nuevoBloque = new Bloque(transacciones);     //O(nb)
        this.blockchain.add(nuevoBloque);                   //O(1)
    }
    //***************************************************************************************

    public Transaccion txMayorValorUltimoBloque(){

        // Debe hacerse en O(1)

        Bloque ultimoBloque = this.blockchain.get(blockchain.size()-1);             //O(1) acceso al ultimo de una lista
        Transaccion res = new Transaccion(ultimoBloque.getTxPorMonto().max());      //O(1) acceso al máximo de un heapMax.
        return res;                                                                 //O(1)
    }
    //******************************************************************************************

    public Transaccion[] txUltimoBloque(){

        //Debe hacerse en O(nb)


        Bloque ultimoBloque = this.blockchain.get(blockchain.size()-1);         //O(1)
        ArrayList<Transaccion> transacciones = ultimoBloque.getTxPorId();       //O(nb) (copia lista de transacciones)
        Transaccion[] res = new Transaccion[transacciones.size()];
        for (int i = 0; i < transacciones.size(); i++) {
            res[i] = transacciones.get(i);                                      //O(nb) Copia cada elemento a un array.
        }
        return res;
    }
    //***********************************************************************************************************
    public int maximoTenedor(){

        // Debe hacerese en O(1)
        return heapUsuarios.max().getId();                  // Buscar el máximo en un HeapMax es O(1)
    }
    //***********************************************************************************************************
    public int montoMedioUltimoBloque(){

        //Debe hacerse en O(1)
        Bloque ultimoBloque = this.blockchain.get(blockchain.size()-1);            //O(1)
        if (ultimoBloque.getCantidadTxSinCreacion() == 0){                         //O(1)
            return 0;
        } else {
        int montoMedio = ultimoBloque.getSumaMontosSinCreacion() / ultimoBloque.getCantidadTxSinCreacion();
        return montoMedio;
        }
    }
        //Las cantidades son atributos de la clase bloque, accedemos a ellos en O(1)
    //************************************************************************************************************

    public void hackearTx(){

        //Debe hacerse en O(log nb + log P)

        Bloque ultimo = this.blockchain.get(blockchain.size()-1);                   //O(1)
        Transaccion mayorTx = ultimo.getTxPorMonto().extraerMax();                  //O(log nb)

        if (mayorTx.id_comprador() != 0){
            Usuario comprador = this.usuarios[mayorTx.id_comprador()-1];         //O(1)
            comprador.incremetarSaldo(mayorTx.monto());                          //O(1)
            HeapHandle<Usuario> HandleComprador = comprador.getHandle();            //O(1)
            this.heapUsuarios.update(HandleComprador);                              //O(log P)
        }

        Usuario vendedor = this.usuarios[mayorTx.id_vendedor()-1];               //O(1)
        vendedor.decrementarSaldo(mayorTx.monto());                              //O(1)
        HeapHandle<Usuario> HandleVendedor = vendedor.getHandle();                  //O(1)
        this.heapUsuarios.update(HandleVendedor);                                   //O(log P)
        ultimo.hackearBloque(mayorTx);                                              //O(1)

        // 8 * O(1) + O(log nb) + 2 * O(log P)  =   O(log nb + log P)

    }
}
