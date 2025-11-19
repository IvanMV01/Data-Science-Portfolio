module Tests where
import Test.HUnit
import Solucion


main = runTestTT tests

tests = test (testNombresDeUsuarios ++ testAmigosDe ++ testCantidadDeAmigos ++ testUsuarioConMasAmigos ++ testEstaRobertoCarlos ++ testPublicacionesDe ++ testPublicacionesQueLeGustanA ++ testLesGustanLasMismasPublicaciones ++ testTieneUnSeguidorFiel ++ testExisteSecuenciaDeAmigos ++ testmismoselementos)

--Ejercicio 1
testNombresDeUsuarios = [
    " devuelve los nombres de usuarios de la red sin repetidos" ~: mismoselementos (nombresDeUsuarios red1) ["Pablo", "Juana", "Valentina", "Juan"] ~?= True,
    " una red sin ususarios devuelve []" ~: nombresDeUsuarios redVacia ~?= []]

-- Ejercicio 2
testAmigosDe = [
    " devuelve todos los amigos del usuario" ~: mismoselementos (amigosDe red1 usuario1) [usuario3, usuario4, usuario2] ~?= True,
    " devuelve [] si no hay relaciones" ~: amigosDe redCasiVacia usuario1 ~?= [],
    " un usuario sin amigos devuelve []" ~: amigosDe red2 usuario4 ~?= []]

-- Ejercicio 3
testCantidadDeAmigos = [
    " devuelve la cantidad de amigos del usuario" ~: cantidadDeAmigos red1 usuario1 ~?= 3,
    " si amigosDe del usuario devuelve [] (el usuario no tiene amigos), devuelve 0" ~: cantidadDeAmigos red2 usuario4 ~?= 0]
    
--Ejercicio 4
testUsuarioConMasAmigos = [
    " devuelve el usuario con mas amigos" ~: usuarioConMasAmigos red1 ~?= usuario1 ,
    " devuelve el ultimo usuario con la mayor cantidad de amigos si hay mas de uno" ~: expectAny (usuarioConMasAmigos red2) [usuario3, usuario2],
    " devuelve cualquier usuario si no hay relaciones" ~: expectAny (usuarioConMasAmigos redCasiVacia) usuarios1]

-- Ejercicio 5
testEstaRobertoCarlos = [
    " True: tiene mas de 10 amigos" ~: estaRobertoCarlos redRC ~?= True ,
    " False tiene menos de 10 amigos" ~: estaRobertoCarlos red1 ~?= False ,
    " False: tiene 10 amigos" ~: estaRobertoCarlos redRC2 ~?= False]

-- Ejercicio 6
testPublicacionesDe = [
    " devuelve todas las publicaciones del usuario" ~: mismoselementos (publicacionesDe red1 usuario2) [publicacion3_us2, publicacion2_us2, publicacion1_us2] ~?= True,
    " si el usuario no tiene publicaciones devuelve vacio" ~: publicacionesDe red1 usuario3 ~?= []]

-- Ejercicio 7
testPublicacionesQueLeGustanA = [
    " devuelve todas las publicaciones que le gustan al usuario" ~: mismoselementos (publicacionesQueLeGustanA red1 usuario4) [publicacion1_us2, publicacion1_us1] ~?= True,
    " devuelve vacio si no le gusta ninguna publicacion" ~: publicacionesQueLeGustanA red1 usuario2 ~?= [],
    " devuelve vacio si no hay publicaciones" ~: publicacionesQueLeGustanA redCasiVacia usuario1 ~?= []]

--Ejercicio 8
testLesGustanLasMismasPublicaciones = [
    " True: Les gustan las mismas publicaciones" ~: lesGustanLasMismasPublicaciones red1 usuario1 usuario4 ~?= True ,
    " False: Tienen algunas pero no todas las publicaciones que les gustan en comun" ~: lesGustanLasMismasPublicaciones red1 usuario1 usuario3 ~?= False,
    " False: A un usuario no le gusta ninguna publicacion y al otro si" ~: lesGustanLasMismasPublicaciones red1 usuario1 usuario2 ~?= False,
    " True: A ninguno de los dos usuarios le gusta ninguna publicacion" ~: lesGustanLasMismasPublicaciones red1 usuario2 usuario5R ~?= True]

--Ejercicio 9
testTieneUnSeguidorFiel = [
    " True: existe un alguien que le gusten todas las publicaciones" ~: tieneUnSeguidorFiel red1 usuario2 ~?= True ,
    " Fales: no se cumple la condicion" ~: tieneUnSeguidorFiel red1 usuario1 ~?= False,
    " False: red no tiene publicaciones" ~: tieneUnSeguidorFiel redCasiVacia usuario1 ~?= False]

-- Ejercicio 10
testExisteSecuenciaDeAmigos = [
    " True: Existe cadena de amigos posible empezando con u1 y terminando con u2 " ~: existeSecuenciaDeAmigos red1 usuario1 usuario3 ~?= True,
    " True: u1 y u2 son amigos " ~: existeSecuenciaDeAmigos red1 usuario1 usuario3 ~?= True,
    " True: Existe aunque haya que pasar por varios amigos" ~: existeSecuenciaDeAmigos red4 usuario2 usuario7 ~?= True,
    " False: no existe cadena posible que cumpla" ~: existeSecuenciaDeAmigos red3 usuario2 usuario4 ~?= False,
    " False: u2 no tiene amigos" ~: existeSecuenciaDeAmigos red2 usuario3 usuario4 ~?= False,
    " False: u1 no tiene amigos" ~: existeSecuenciaDeAmigos red2 usuario4 usuario2 ~?= False,
    " False: La red no tiene relaciones" ~: existeSecuenciaDeAmigos redCasiVacia usuario1 usuario2 ~?= False]

--mismoselementos
testmismoselementos = [
    "True: las 2 listas contienen los mismos elementos" ~: mismoselementos [1,2,3,4] [1,2,3,4] ~?= True ,
    "True: aunque esten en distinto orden" ~: mismoselementos [1,2,3,4] [2,3,1,4] ~?= True ,
    "False: si las listas no contienen los mismos elementos" ~: mismoselementos [1,2,3,4] [3,6,9,8] ~?= False ,
    "False: una de las listas este incluida en la otra pero no viceversa" ~: mismoselementos [1,2,3] [1,2,3,4] ~?= False]

expectAny actual expected = elem actual expected ~? ("expected any of: " ++ show expected ++ "\n but got: " ++ show actual)

usuario1 :: Usuario
usuario1 = (1, "Pablo")
usuario2 :: Usuario
usuario2 = (2, "Juan")
usuario3 :: Usuario
usuario3 = (3, "Juana")
usuario4 :: Usuario
usuario4 = (4, "Valentina")
usuario5R :: Usuario
usuario5R = (5, "Juan")


usuarios1 :: [Usuario]
usuarios1 = [usuario1, usuario2, usuario3, usuario4, usuario5R]
usuarios2 :: [Usuario]
usuarios2 = [usuario1, usuario2, usuario3, usuario4, usuario5, usuario6, usuario7]

relacion1 :: Relacion
relacion1 = (usuario1, usuario3)
relacion2 :: Relacion
relacion2 = (usuario2, usuario3)
relacion3 :: Relacion
relacion3 = (usuario1, usuario4)
relacion4 :: Relacion
relacion4 = (usuario2, usuario1)
relacion5 :: Relacion
relacion5 = (usuario1,usuario5)
relacion6 = (usuario2, usuario5)
relacion7 = (usuario1, usuario7)
relacion8 = (usuario4, usuario7)

relaciones1 :: [Relacion]
relaciones1 = [relacion1, relacion2, relacion3, relacion4]
relaciones2 :: [Relacion]
relaciones2 = [relacion1, relacion2, relacion4]
relaciones3 :: [Relacion]
relaciones3 = [relacion3, relacion2]
relaciones4 :: [Relacion]
relaciones4 = [relacion2, relacion7, relacion5, relacion6, relacion8]


publicacion1_us1 :: Publicacion
publicacion1_us1 = (usuario1, "primer post", [usuario1, usuario4])
publicacion2_us1 :: Publicacion
publicacion2_us1 = (usuario1, "segundo post", [usuario3])

publicacion1_us2 :: Publicacion
publicacion1_us2 = (usuario2, "primer post", [usuario1, usuario4, usuario3])
publicacion2_us2 :: Publicacion
publicacion2_us2 = (usuario2, "segundo post", [usuario3])
publicacion3_us2 :: Publicacion
publicacion3_us2 = (usuario2, "tercer post", [usuario3])


publicaciones1 :: [Publicacion]
publicaciones1 = [publicacion3_us2, publicacion2_us2, publicacion1_us2, publicacion2_us1, publicacion1_us1]

red1 :: RedSocial
red1 = (usuarios1, relaciones1, publicaciones1)
red2 :: RedSocial
red2 = (usuarios1, relaciones2, publicaciones1)
red3 :: RedSocial
red3 = (usuarios1, relaciones3, publicaciones1)
red4 = (usuarios2, relaciones4, [])
redCasiVacia :: RedSocial
redCasiVacia = (usuarios1, [], [])
redVacia :: RedSocial
redVacia = ([], [], [])

-- Roberto Carlos
-- usuarios para Roberto Carlos
usuario5 = (5, "Martin")
usuario6 = (6, "Nicolas")
usuario7 = (7, "Martina")
usuario8 = (8, "Felipe")
usuario9 = (9, "Julia")
usuario10 = (10, "Ariel")
usuario11 = (11, "Katia")
usuario12 = (12, "Franco")
robertoCarlos = (13, "Roberto Carlos")

usuariosRC :: [Usuario]
usuariosRC = [usuario1, usuario2, usuario3, usuario4, usuario5, usuario6, usuario7, usuario8, usuario9, usuario10, usuario11, usuario12, robertoCarlos]

-- Relaciones para roberto Carlos
relacionRC1 = (robertoCarlos, usuario2)
relacionRC2 = (robertoCarlos, usuario3)
relacionRC3 = (robertoCarlos, usuario4)
relacionRC4 = (robertoCarlos, usuario5)
relacionRC5 = (robertoCarlos, usuario6)
relacionRC6 = (robertoCarlos, usuario7)
relacionRC7 = (robertoCarlos, usuario8)
relacionRC8 = (robertoCarlos, usuario9)
relacionRC9 = (robertoCarlos, usuario10)
relacionRC10 = (robertoCarlos, usuario11)
relacionRC11 = (robertoCarlos, usuario12)

-- Relaciones para roberto Carlos
relacionesRC :: [Relacion]
relacionesRC = [relacionRC1, relacionRC2, relacionRC3, relacionRC4, relacionRC5, relacionRC6, relacionRC7, relacionRC8, relacionRC9, relacionRC10, relacionRC11]
relacionesRC2 :: [Relacion]
relacionesRC2 = [relacionRC1, relacionRC2, relacionRC3, relacionRC4, relacionRC5, relacionRC6, relacionRC7, relacionRC8, relacionRC9, relacionRC10]

-- Red para Roberto Carlos
redRC = (usuariosRC, relacionesRC, [])
redRC2 = (usuariosRC, relacionesRC2, [])


