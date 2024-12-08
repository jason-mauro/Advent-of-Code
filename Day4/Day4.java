import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Arrays;

public class Day4 {
    public static int findXMASPart2(ArrayList<String> rows, int i, int j){

        boolean left = false;
        boolean right = false;
        // left to right : M A S, S A M

        if (rows.get(i - 1).charAt(j - 1) == 'M' && rows.get(i + 1).charAt(j + 1) == 'S'){
            left = true;
        } else if (rows.get(i - 1).charAt(j - 1) == 'S' && rows.get(i + 1).charAt(j + 1) == 'M'){
            left = true;
        }

        if (rows.get(i - 1).charAt(j + 1) == 'M' && rows.get(i + 1).charAt(j - 1) == 'S'){
            right = true;
        } else if (rows.get(i - 1).charAt(j + 1) == 'S' && rows.get(i + 1).charAt(j - 1) == 'M'){
            right = true;
        }

        // right to left : M A S, S A M
        return left && right ? 1 : 0;
    }

    public static int findXMASPart1(ArrayList<String> rows, int i, int j){
        int total = 0;
        // Search Horizontal
        if(j <= rows.get(i).length() - 4 && rows.get(i).substring(j, j+4).equals("XMAS")){
            
            total++;
        }


        if (j >= 3 && rows.get(i).substring(j - 3, j + 1).equals("SAMX")){
            total++;
            

        }
        // Search Vertical
        if (i >= 3){
            if (rows.get(i - 3).charAt(j) == 'S' && rows.get(i - 2).charAt(j) == 'A' && rows.get(i - 1).charAt(j) == 'M' ){
                total++;
                
            }
        }
        if (i <= rows.size() - 4){
            if (rows.get(i + 3).charAt(j) == 'S' && rows.get(i + 2).charAt(j) == 'A' && rows.get(i +1).charAt(j) == 'M' ){
                total++;
                
            }
        }


        // Up Right
        if (i >= 3 && j <= rows.get(i).length() - 4 ){
            if(rows.get(i - 1).charAt(j+1) == 'M' && rows.get(i - 2).charAt(j + 2) == 'A' && rows.get(i -3).charAt(j+3) == 'S'){
                total++;
            }
        }
        // up left
        if (i >= 3 && j >= 3){
            if(rows.get(i - 1).charAt(j-1) == 'M' && rows.get(i - 2).charAt(j - 2) == 'A' && rows.get(i - 3).charAt(j-3) == 'S'){
                total++;
            }
        }
        // Down right
        if (i <= rows.size() - 4 && j <= rows.get(i).length() - 4){
            if(rows.get(i + 1).charAt(j+1) == 'M' && rows.get(i + 2).charAt(j + 2) == 'A' && rows.get(i + 3).charAt(j+3) == 'S'){
                total++;
            }
        }

        // down left
        if (i <= rows.size() - 4 && j >= 3){
            if(rows.get(i + 1).charAt(j-1) == 'M' && rows.get(i + 2).charAt(j - 2) == 'A' && rows.get(i + 3).charAt(j-3) == 'S'){
                total++;
            }
        }
        return total;
    }

    public static void main(String[] args) {
        String input = "";
        try {
            Path filePath = Path.of("C:\\Users\\Jason\\IdeaProjects\\AoC\\src\\input.txt");
            input  = Files.readString(filePath);
        } catch (IOException e) {
            System.out.println("File not found");
        }

       ArrayList<String> rows = new ArrayList<String>(Arrays.stream(input.split("\n")).toList());
       int total1 = 0;
       int total2 = 0;

        // Part 1
        for (int i = 0; i < rows.size(); i++) {
            for (int j = 0; j < rows.get(i).length(); j++) {
                if (rows.get(i).charAt(j) == 'X'){
                    total1 += findXMASPart1(rows, i , j);
                }
            }
        }
        System.out.println(total1);


       // Start on Second row and go to the second to last
       for (int i = 1; i < rows.size() - 1; i++) {
           for (int j = 1; j < rows.get(i).length() - 1; j++) {
               if (rows.get(i).charAt(j) == 'A'){
                   total2 += findXMASPart2(rows, i , j);
               }
           }
       }

        System.out.println(total2);

    }
}
