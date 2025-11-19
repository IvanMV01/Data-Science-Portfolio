package aed;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;

public class TestsPropios{

    Berretacoin bc;
    Transaccion[] transacciones1;
    Transaccion[] transacciones2;
    Transaccion[] transacciones3;

    @BeforeEach
        void setUp() {
            bc = new Berretacoin(5);

            transacciones1 = new Transaccion[] {
                new Transaccion(0, 0, 1, 10), // Creación $10 a 1
                new Transaccion(1, 1, 2, 5),  // 1 da $5 a 2
                new Transaccion(2, 2, 3, 3)   // 2 da $3 a 3
            };

            transacciones2 = new Transaccion[] {
                new Transaccion(0, 0, 4, 7), // Creación $7 a 4
                new Transaccion(1, 4, 5, 2), // 4 da $2 a 5
                new Transaccion(2, 5, 1, 1)  // 5 da $1 a 1
            };

            transacciones3 = new Transaccion[] {
                new Transaccion(0, 0, 2, 4), // Creación $4 a 2
                new Transaccion(1, 2, 3, 2), // 2 da $2 a 3
                new Transaccion(2, 3, 4, 4), // 3 da $4 a 4
                new Transaccion(3, 4, 5, 1)  // 4 da $1 a 5
            };

            bc.agregarBloque(transacciones1);
            bc.agregarBloque(transacciones2);
            bc.agregarBloque(transacciones3);

            //Saldos: 1=$6, 2=$4, 3=$1, 4=$8, 5=$2
        }

    @Test
    public void txMayorValorUltimoBloque() {
        Transaccion res = bc.txMayorValorUltimoBloque();

        assertEquals(4, res.monto());
        assertEquals(2, res.getId());
    }

    @Test
    public void txUltimoBloque() {
        Transaccion[] res = bc.txUltimoBloque();

        assertEquals(4, res.length);
        assertEquals(4, res[0].monto());
        assertEquals(3, res[2].id_comprador());
        assertEquals(5, res[3].id_vendedor());
    }

    @Test
    public void maximoTenedor() {
        int res = bc.maximoTenedor();

        assertEquals(4, res);
    }

    Berretacoin moneda;
    Transaccion[] transacciones4;
    Transaccion[] transacciones5;

    @BeforeEach
    void setup() {
        moneda = new Berretacoin(10);
        //crear 10 bloques con solo transacciones de creacion
        transacciones4 = new Transaccion[1];
        for (int i = 0; i<10 ; i++){
            int montoCreacion = 10*(10-i);  // 100 al 1, 90 al 2, etc...
            Transaccion transaccion = new Transaccion(i,0,i+1,montoCreacion);
            transacciones4[0] = transaccion;
            moneda.agregarBloque(transacciones4);

        }

    }
    @Test
    public void soloCreacion(){
        assertEquals(1,moneda.maximoTenedor());
        assertEquals(10,moneda.txMayorValorUltimoBloque().monto());
        assertEquals(0, moneda.montoMedioUltimoBloque()); // porque es solo de creación y no cuentan
    }
    @Test void todosAUno(){
        transacciones5 = new Transaccion[9];
        for (int i = 0 ; i<9; i++){
            Transaccion transaccion = new Transaccion(i,i+1,10,10);
            transacciones5[i] = transaccion;
        }
        moneda.agregarBloque(transacciones5);
        // saldos = [90,80,70,60,50,40,30,20,10,100]
        assertEquals(10, moneda.maximoTenedor());
        assertEquals(10, moneda.montoMedioUltimoBloque());

        moneda.hackearTx();
        assertEquals(1,moneda.maximoTenedor());
        moneda.hackearTx();
        assertEquals(1,moneda.maximoTenedor());
    }

}
