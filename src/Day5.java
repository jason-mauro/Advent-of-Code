import java.io.IOException;
import java.util.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.stream.Collectors;


public class Day5 {





    public static void main(String[] args) {
        List<String> lines = new ArrayList<>();
        try {
            Path filePath = Path.of("C:\\Users\\Jason\\IdeaProjects\\AoC\\src\\input.txt");
            lines = Files.readAllLines(filePath);
        } catch (IOException e) {
            System.out.println("File not found");
        }

        HashMap<Integer, ArrayList<Integer>> orders = new HashMap<>();

        List<String> x = lines.stream()
                .filter(line -> line.contains("|"))
                .collect(Collectors.toList());

        // HashMap for orderings
        for(var j : x){
            var y = j.split("[|]");
            if (!orders.containsKey(Integer.parseInt(y[0]))){
                orders.put(Integer.parseInt(y[0]), new ArrayList<>(){{this.add(Integer.parseInt(y[1]));}});
            } else {
                orders.get(Integer.parseInt(y[0])).add(Integer.parseInt(y[1]));
            }
        }

        List<String> nums = lines.stream()
                .filter(line -> line.contains(","))
                .collect(Collectors.toList());

        int total = 0;
        int total2 = 0;
        for (var l : nums){
            ArrayList<Integer> pages = new ArrayList<Integer>(Arrays.stream(l.split(",")).map(Integer::parseInt).toList());
            boolean valid = true;
            boolean swapped = true;
            while(swapped) {
                swapped = false;
                for (int i = 0; i < pages.size(); i++) {
                    if (orders.containsKey(pages.get(i))) {
                        for (int o : orders.get(pages.get(i))) {
                            if (pages.contains(o)) {
                                int index = pages.indexOf(o);
                                if (i > index) {
                                    Collections.swap(pages, index, i);
                                    swapped = true;
                                    valid = false;
                                }
                            }
                        }
                    }
                }
            }
            if (valid) {
                total += pages.get(pages.size() / 2 );
            } else {
                total2 += pages.get(pages.size() / 2 );
            }
        }
        System.out.println(total);
        System.out.println(total2);
    }
}
