package aed;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class UsuarioTests {

    @Test
    void usuarioTieneSaldoeId() {
        Usuario usuario = new Usuario(1,3);
        assertEquals(1,usuario.getId());
        assertEquals(3,usuario.getSaldo());
    }
    @Test
    void usuarioVariaSaldo() {
        Usuario usuario = new Usuario(1,1);
        usuario.incremetarSaldo(3);
        assertEquals(4,usuario.getSaldo());
        usuario.decrementarSaldo(2);
        assertEquals(2,usuario.getSaldo());
    }

    @Test
    void usuarioCompareSaldos() {
        Usuario usuario1 = new Usuario(1,1);
        Usuario usuario2 = new Usuario(2,2);
        Usuario usuario3 = new Usuario(2,2);
        assertTrue(0 < usuario2.compareTo(usuario1));
        assertTrue(0 > usuario1.compareTo(usuario2));
        assertTrue(0 == usuario2.compareTo(usuario3));
    }

    @Test
    void usuarioCompareId () {
        Usuario usuario1 = new Usuario(1,1);
        Usuario usuario2 = new Usuario(2,1);

        assertTrue(0 > usuario2.compareTo(usuario1));
        assertTrue(0 < usuario1.compareTo(usuario2));
    }




}