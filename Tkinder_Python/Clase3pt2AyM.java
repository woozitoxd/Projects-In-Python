import java.util.Scanner;
import java.time.LocalDate;

public class AlumnoNotas {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Ingrese el nombre del alumno: ");
        String nombre = sc.nextLine();

        System.out.print("Ingrese el año de nacimiento del alumno: ");
        int anioNacimiento = sc.nextInt();

        // calculo edad con la fecha actual
        int anioActual = LocalDate.now().getYear();
        int edad = anioActual - anioNacimiento;

        // pido notas para sacar promedio
        System.out.print("Ingrese nota 1: ");
        int nota1 = sc.nextInt();
        System.out.print("Ingrese nota 2: ");
        int nota2 = sc.nextInt();

        double promedio = (nota1 + nota2 ) / 2.0;

        // Mmuestro resultados
        System.out.println("\nAlumno: " + nombre);
        System.out.println("Edad: " + edad);
        System.out.println("Promedio: " + promedio);

        if (promedio >= 6 && edad >= 18) {
            System.out.println("Resultado: APROBADO (mayor de edad y con promedio suficiente)");
        } else if (promedio >= 6) {
            System.out.println("Resultado: APROBADO (pero es menor de edad)");
        } else {
            System.out.println("Resultado: DESAPROBADO");
        }
        sc.close();
    }
}