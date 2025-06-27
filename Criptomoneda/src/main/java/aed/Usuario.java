package aed;

class Usuario implements Priorizable<Usuario> {
    private int id;
    private int saldo;
    private HeapHandle<Usuario> handle;

    public Usuario(int id, int saldo){
        this.id = id;
        this.saldo = saldo;
    }

    public Usuario (Usuario otro){
        this.id = otro.getId();
        this.saldo = otro.getSaldo();
    }

    public Usuario copy(){
        Usuario copia = new Usuario(this);
        return copia;
    }

    public void setSaldo(int valor) {
        this.saldo = valor;
    }

    public int getSaldo() {
        return this.saldo;
    }

    public void incremetarSaldo(int valor){
        this.saldo += valor;
    }
    public void decrementarSaldo(int valor){
        this.saldo -= valor;
    }

    public int getId(){
        return this.id;
    }



    public int compareTo(Usuario otro){
        if (this.saldo > otro.saldo) {
            return 1;
        } else if (this.saldo < otro.saldo) {
            return -1;
        } else {
            if (this.id > otro.id) {
                return -1;
            } else if (this.id < otro.id) {
                return 1;
            } else {
                return 0;
            }
        }
    }

    public void setHandle(HeapHandle<Usuario> handle){
        this.handle = handle;
    }

    public HeapHandle<Usuario> getHandle(){
        return this.handle;
    }
}
