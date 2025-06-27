package aed;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;

public class HeapTests{

    public int[] intercalados(int n, int k){
        int[] res = new int[n];
        for (int i = 0; i<n ; i++ ){
            if (i%2 == 0){
                res[i] = k*(n-1-i);
            }else{
                res[i] = k*(i-1);
            }
        }
        return res;
    }

    public int[] decreciente(int n, int k){
        int[] res = new int [n];
        for (int i = 0; i<n ; i++){
            res [i] = k*(n-1-i);
        }
        return res;
    }



    public ArrayList<Usuario> crearUsuarios(int n, int[] saldos){
        ArrayList<Usuario> res = new ArrayList<Usuario>(n);
        for (int i=0; i<n; i++){
            Usuario usuario = new Usuario(i+1,saldos[i]);
            res.add(usuario);
        }

        System.out.println(Arrays.toString(saldos));
        return res;
    }

    @Test
    public void heapDeUsuariosPorCopiaDeLista(){
        int[] saldos_intercalados = intercalados(10 ,500);
        ArrayList<Usuario> usuarios_intercalados = crearUsuarios(10, saldos_intercalados);

        int[] saldos_decrecientes = decreciente(10, 500);
        ArrayList<Usuario> usuarios_decrecientes = crearUsuarios(10, saldos_decrecientes);

        Heap<Usuario> usuarioHeap = new Heap<Usuario>(usuarios_intercalados);

        for (int i =0 ; i< usuarios_decrecientes.size(); i++){
            assertEquals(usuarioHeap.extraerMax().getSaldo(), usuarios_decrecientes.get(i).getSaldo());

        }
    }
    @Test
    public void HeapDeTransaccionesConMontoRepetido(){

        Transaccion[] transacciones;
        transacciones = new Transaccion[] {
                new Transaccion(0, 0, 2, 1),
                new Transaccion(1, 2, 3, 14),
                new Transaccion(2, 0, 2, 133),
                new Transaccion(3, 2, 3, 321),
                new Transaccion(4, 0, 2, 413),
                new Transaccion(5, 2, 3, 1500),
                new Transaccion(6, 0, 2, 100),
                new Transaccion(7, 2, 3, 100),
                new Transaccion(8, 0, 2, 100),
                new Transaccion(9, 2, 3, 130),
                new Transaccion(10, 3, 4, 160)
        };

        int[] heapificadoPorId = {5,4,2,3,10,0,6,7,8,9,1};

        Heap<Transaccion> heapTransacciones = new Heap<Transaccion>(transacciones);

        ArrayList<Transaccion> transaccionesHeapificadas = heapTransacciones.getData();

        for (int i=0; i<transaccionesHeapificadas.size(); i++){
            assertEquals(heapificadoPorId[i],transaccionesHeapificadas.get(i).getId());
        }



    }


}