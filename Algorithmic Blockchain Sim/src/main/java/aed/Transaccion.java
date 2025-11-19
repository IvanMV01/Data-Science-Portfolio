package aed;

public class Transaccion implements Priorizable<Transaccion> {
    private int id;
    private int id_comprador;
    private int id_vendedor;
    private int monto;
    private HeapHandle<Transaccion> handle;

    public Transaccion(int id, int id_comprador, int id_vendedor, int monto) {
        this.id = id;
        this.id_comprador = id_comprador;
        this.id_vendedor = id_vendedor;
        this.monto = monto;
    }

    public Transaccion(Transaccion otra){
        this.id = otra.getId();
        this.id_comprador = otra.id_comprador();
        this. id_vendedor = otra.id_vendedor();
        this.monto = otra.monto();
    }
    public Transaccion copy(){
        Transaccion copia = new Transaccion(this);
        return copia;
    }

    public boolean esCreacion(){
        return this.id_comprador == 0;
    }

    
    @Override
    public int compareTo(Transaccion otro) {
        if (this.monto > otro.monto) {
            return 1;
        } else if (this.monto < otro.monto) {
            return -1;
        } else {
            if (this.id > otro.id) {
                return 1;
            } else if (this.id < otro.id) {
                return -1;
            } else {
                return 0;
            }
        }
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;

        Transaccion otra = (Transaccion) obj;
        return this.id == otra.id;
    }

    public int monto() {
        return monto;
    }

    public int id_comprador() {
        return id_comprador;
    }
    
    public int id_vendedor() {
        return id_vendedor;
    }

    public void setHandle(HeapHandle<Transaccion> handle){
        this.handle = handle;
    }

    public int getId(){
        return this.id;
    }

    public HeapHandle<Transaccion> getHandle(){
        return this.handle;
    }

}