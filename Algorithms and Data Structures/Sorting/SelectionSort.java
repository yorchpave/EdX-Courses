import java.util.Arrays;

/**
    Selection sort is a sorting algorithm that looks
    for the smallest value in an array (inner for loop)
    and swaps it with the value at the current index (outter for loop).
*/

public class SelectionSort{

    public static void main(String[] args) {

       int[] myArray = {4, 9, 7, 1, 3, 6, 5};

       System.out.print("Array to sort using selection sort: ");
       System.out.println(Arrays.toString(myArray));
       System.out.print("Array after sorting: ");
       SelectionSort(myArray);
    }

    public static void SelectionSort(int[] myArray){

        int smallest = 0; // Smallest value
        int minIndex = 0; // Index of smallest value
        int n = myArray.length; // Size of array

        for(int i = 0; i < n - 1; i++){

            smallest = myArray[i]; // Assume that current value is smallest
            minIndex = i; // Assume that current index is smallest
            for(int j = i + 1; j < n; j++){

                if(myArray[j] < smallest){

                    smallest = myArray[j]; //Update smallest value
                    minIndex = j; // Index of found smallest value
                }
            }
            // Swap values after smallest value and index is found
            int temp = myArray[i];
            myArray[i] = smallest;
            myArray[minIndex] = temp;
        }

        System.out.println(Arrays.toString(myArray)); // Print sorted array
    }
}
