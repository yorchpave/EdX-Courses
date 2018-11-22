/**
   Binary search is an algorithm that looks a specific
   element in an array. The array has to be already sorted.
   It look for the element by looking at the element at the
   middle of the array, if it matches it finishes, if not
   it compares the value with the element: if the value is
   smaller then look at left half of the array and repeat the process.
   If the value is bigger it does the same thing but looks at
   the right half of the array.
*/

public class BinarySearch{


    public static void main(String[] args) {

        int[] myArray = {1, 3, 4, 5, 7, 9, 13, 15, 16, 17, 19}; 
        int left = 0;
        int right = myArray.length - 1;

        binarySearch(15, myArray, left, right); // Insert value you want to find

    }

    public static void binarySearch( int x, int[] myArray, int left, int right){

        if(left > right){ // This means that the method has already looked
                          // over the entire array

            System.out.println("Element is not in the array");
            return;
        }
        // Update the middle value/index as the array changes
        int middle = (left + right) / 2;

        if(myArray[middle] == x){

            System.out.println("Found " + x + " at index: " + middle);
        }

        else if(x < myArray[middle]){
            // Shrink the array by moving the end of the array
            // to the middle - 1 position
            right = middle - 1;
            // Recursion call with same array but updated boundaries
            binarySearch(x, myArray, left, right);
        }

        else if(x > myArray[middle]){
            // Shrink the array by moving the beginning of the array
            // to the middle + 1 position
            left = middle + 1;
            // Recursion call with same array but updated boundaries
            binarySearch(x, myArray, left, right);

        }
    }
}
