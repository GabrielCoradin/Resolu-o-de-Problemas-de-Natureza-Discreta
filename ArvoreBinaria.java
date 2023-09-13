import java.util.Scanner;

public class ArvoreBinaria {

  public static int busca_binaria(int dado[], int x, int inferior, int superior) {
    int meio;
    if (inferior > superior) {
      return -1;
    }
    meio = (inferior + superior) / 2;
    if (x == dado[meio]) {
      return meio;
    }
    if (x < dado[meio]) {
      return busca_binaria(dado, x, inferior, meio - 1);
    } else {
      return busca_binaria(dado, x, meio + 1, superior);
    }
  }

  public static void bubbleSort(int[] arr) {
    int n = arr.length;
    for (int i = 0; i < n - 1; i++) {
      for (int j = 0; j < n - i - 1; j++) {
        if (arr[j] > arr[j + 1]) {
          int temp = arr[j];
          arr[j] = arr[j + 1];
          arr[j + 1] = temp;
        }
      }
    }
  }

  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);

    System.out.println("Digite o tamanho do vetor:");
    int n = scan.nextInt();
    int[] dado = new int[n];
    System.out.println("Digite os elementos do vetor:");

    for (int i = 0; i < n; i++) {
      dado[i] = scan.nextInt();
    }

    bubbleSort(dado);

    System.out.println("Qual elemento deseja encontrar?");
    int valor = scan.nextInt();
    int inf = 0;
    int sup = dado.length - 1;
    int funcao = busca_binaria(dado, valor, inf, sup);

    if (funcao == -1) {
      System.out.println("Nao existe esse elemento no vetor");
    } else {
      System.out.println("Elemento encontrado no indice: " + funcao);
    }
    scan.close();
  }
}