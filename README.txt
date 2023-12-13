
--1)	Crear un bloque de plsql que muestre todos los nombres de los estudiantes
--junto con la cantidad de préstamos de libros que tiene cada uno de ellos.

SET SERVEROUTPUT ON;

DECLARE
   v_nombre_estudiante estudiante.nombre%TYPE;
   v_cantidad_prestamos NUMBER;
   
   CURSOR c_estudiantes IS
      SELECT cod_est, nombre
      FROM estudiante;
BEGIN
   FOR estudiante_rec IN c_estudiantes LOOP
      -- Inicializar la variable de cantidad de préstamos
      v_cantidad_prestamos := 0;
      
      -- Consultar la cantidad de préstamos para el estudiante actual
      SELECT COUNT(*)
      INTO v_cantidad_prestamos
      FROM prestamo
      WHERE cod_est = estudiante_rec.cod_est;
      
      -- Mostrar el resultado
      DBMS_OUTPUT.PUT_LINE('Estudiante: ' || estudiante_rec.nombre || ', Cantidad de Préstamos: ' || v_cantidad_prestamos);
   END LOOP;
END;
/

-- 2 2)	Crear un bloque de plsql que solicite un código de estudiante y muestre 
--cuando fue la última fecha donde solicito un préstamo de libro (fecha_prest), 
--si no tiene prestamos, se debe indicar esto con la frase “no tiene prestamos”

SET SERVEROUTPUT ON;

DECLARE
   v_cod_estudiante estudiante.cod_est%TYPE;
   v_fecha_ultimo_prestamo prestamo.fecha_prest%TYPE;
BEGIN
   -- Solicitar el código de estudiante
   v_cod_estudiante := &codigo_estudiante; -- Utiliza el símbolo & para solicitar la entrada del usuario

   -- Buscar la última fecha de préstamo para el estudiante
   SELECT MAX(fecha_prest)
   INTO v_fecha_ultimo_prestamo
   FROM prestamo
   WHERE cod_est = v_cod_estudiante;

   -- Mostrar el resultado
   IF v_fecha_ultimo_prestamo IS NOT NULL THEN
      DBMS_OUTPUT.PUT_LINE('La última fecha de préstamo para el estudiante ' || v_cod_estudiante || ' fue el ' || TO_CHAR(v_fecha_ultimo_prestamo, 'DD-MON-YYYY'));
   ELSE
      DBMS_OUTPUT.PUT_LINE('El estudiante ' || v_cod_estudiante || ' no tiene préstamos.');
   END IF;
END;
/


--3)Crear un bloque de plsq que muestre el o los nombres de autor con la mayor 
--cantidad de préstamos. (40 Puntos)

SET SERVEROUTPUT ON;

DECLARE
   v_cod_autor_mas_prestamos autor.cod_autor%TYPE;
   v_max_prestamos NUMBER := 0;

   CURSOR c_autores IS
      SELECT a.cod_autor, a.nombre_autor, COUNT(*) as cantidad_prestamos
      FROM autor a
           JOIN libro l ON a.cod_autor = l.cod_autor
           JOIN prestamo p ON l.cod_libro = p.cod_libro
      GROUP BY a.cod_autor, a.nombre_autor
      ORDER BY cantidad_prestamos DESC;
BEGIN
   -- Obtener el autor con la mayor cantidad de préstamos
   OPEN c_autores;
   FETCH c_autores INTO v_cod_autor_mas_prestamos, v_max_prestamos;
   CLOSE c_autores;

   -- Mostrar el resultado
   IF v_cod_autor_mas_prestamos IS NOT NULL THEN
      DBMS_OUTPUT.PUT_LINE('Autor con la mayor cantidad de préstamos: ' || v_cod_autor_mas_prestamos || ' - ' || v_max_prestamos || ' préstamos');
   ELSE
      DBMS_OUTPUT.PUT_LINE('No hay información disponible.');
   END IF;
END;
/

