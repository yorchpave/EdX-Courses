/**
   Linear search is an algorithm that looks for a given
   element in an array. It does this by visiting
   index by index until the element is found.
*/

public class LinearSearch{

    public static void main(String[] args) {

        int[] myArray = {1, 2, 3, 4, 5};
        int x = 5;
        linearSearch(myArray, x);
    }

    public static void linearSearch(int[] myArray, int x){

        int n = myArray.length;

        for(int i = 0; i < n; i++){

            if(myArray[i] == x){

                System.out.println("Found " + x + " at index " + i);
                return;
            }
        }

        System.out.println(x + " is not in the array");
    }
}
