import java.util.Arrays;

/**
    Merge sort is a sorting algorithm that divides an array in halves
    (left and right) recursively. Once all the left and right arrays
    are divided up until 1 element, call helper method to sort them
    and merge them, recursively once again.
*/

public class MergeSort{

    public static void main(String[] args) {

        int[] myArray= {4, 9, 7, 6, 5, 3, 1};
        int[] result = mergeSort(myArray);
        System.out.print("Array to sort using merge sort: ");
        System.out.println(Arrays.toString(myArray));
        System.out.print("Array after sorting: ");
        System.out.println(Arrays.toString(result));

    }

    public static int[] mergeSort(int[] myArray){

        int n = myArray.length;

        if(n <= 1){ // If array is only 1 element, return it

            return myArray;
        }

        int middle = n / 2; // get middle point of array
        //declare new left and right arrays
        int[] left = new int[middle];
        int[] right;

        if(n % 2 != 0){
            // If right half is odd, right array will be bigger by 1
            right = new int[middle + 1];

        } else{
            // If right half is even, right array will be same size
            right = new int[middle];
        }

        for(int i = 0; i < middle; i++){
            // Populate left array until half of array is reached
            left[i] = myArray[i];
        }

        for(int j = 0; j < right.length; j++){
            // Populate right array from middle until end of array is reached
            right[j] = myArray[middle + j];
        }

        int[] result = new int[n]; // Declare new array that will hold result

        // Recursive call until it is done splitting
        // left and right subarrays
        left = mergeSort(left);
        right = mergeSort(right);
        // Call helper method that will merge left and right
        // arrays from bottom to top (all left and right subarrays
        // that stacked up)
        result = merge(left, right);

        return result; // Return sorted array
    }

    // Helper method in charge of merging and sorting the arrays
    public static int[] merge(int[] left, int[] right){

        int[] result = new int[left.length + right.length];
        int leftPointer, rightPointer, resultPointer;
        leftPointer = rightPointer = resultPointer = 0;
        // Check if any of the two arrays have not been traversed entirely
        while(leftPointer < left.length || rightPointer < right.length){
            // If both arrays have not finished traversing
            // then compare their elements and sort them into the result array
            if(leftPointer < left.length && rightPointer < right.length){

                if(left[leftPointer] < right[rightPointer]){

                    result[resultPointer] = left[leftPointer];
                    resultPointer++;
                    leftPointer++;

                } else{

                    result[resultPointer] = right[rightPointer];
                    resultPointer++;
                    rightPointer++;
                }
            // If only the left array has not finished traversing entirely
            // just populate the result array
            } else if(leftPointer < left.length){

                result[resultPointer] = left[leftPointer];
                resultPointer++;
                leftPointer++;
            // If only the right array has not finished traversing entirely
            // just populate the result array
            } else if(rightPointer < right.length){

                result[resultPointer] = right[rightPointer];
                resultPointer++;
                rightPointer++;
            }
        } // End of while loop

        return result; // Return sorted array
    }
}
