import java.util.Arrays;

/**
    Bubble sort is a sorting algorithm that compares the
    elements in an array(2 by 2) and swaps them accordingly.
    It depends on how you want the array to be sorted (increasing
    or decreasing order). It repeats this process until the array is
    finally sorted.
*/

public class BubbleSort{

    public static void main(String[] args) {

        int[] myArray = {4, 9, 7, 1, 3, 6, 5};
        System.out.print("Array to sort using bubble sort: ");
        System.out.println(Arrays.toString(myArray));
        System.out.print("Array after sorting: ");
        bubbleSort(myArray);
    }

    public static void bubbleSort(int[] myArray){

        int n = myArray.length; // Size of array
        int temp = 0; // IInitialize temporary variable
        boolean doneSwapping = true; // Initialize boolean variable

        do{
            doneSwapping = true; // Assume there will not be any swapping

            for(int i = 0; i < n -1; i++){

                if(myArray[i] > myArray[i + 1]){
                    // Swap elements
                    temp = myArray[i];
                    myArray[i] = myArray[i + 1];
                    myArray[i + 1] = temp;
                    // Set boolean variable to false. Some swapping was done
                    doneSwapping = false;
                }
            }
        } while(doneSwapping == false); // Will become true if there was no swapping,
                                        // meaning the array is finally sorted

        System.out.println(Arrays.toString(myArray));
    }
}
