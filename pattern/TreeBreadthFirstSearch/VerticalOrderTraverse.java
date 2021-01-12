import java.util.Map;
import java.util.TreeMap;
import java.util.Vector;

/**
 Given a binary tree, print it vertically. The following example illustrates the vertical order traversal.
                        1
                     /    \
                    2      3
                    / \   /   \
                   4   5  6   7
                             /  \
                             8   9
 The output of print this tree vertically will be:
 4
 2
 1 5 6
 3 8
 7
 9
 */
public class VerticalOrderTraverse {
    public static class Node{
        int key;
        Node left;
        Node right;

        public Node(int key) {
            this.key = key;
        }
    }

    private static void getVerticalOrder(Node root, int hd, TreeMap<Integer, Vector<Integer>> map){
        // base case
        if(root == null)
            return;

        // get the vector list at 'hd'
        Vector<Integer> getHd = map.get(hd);

        // Store current node in map
        if(getHd == null){
            getHd = new Vector<>();
            getHd.add(root.key);
        }else
            getHd.add(root.key);

        map.put(hd,getHd);

        //Store nodes in the left/right subtree
        getVerticalOrder(root.left,hd-1,map);
        getVerticalOrder(root.right,hd+1,map);
    }

    public static void getVerticalOrder(Node root){
        TreeMap<Integer, Vector<Integer>> map = new TreeMap<>();
        getVerticalOrder(root,0,map);

        for(Map.Entry<Integer,Vector<Integer>> entry: map.entrySet()){
            System.out.println(entry.getValue());
        }
    }

    public static void main(String[] args){
        Node root = new Node(1);
        root.left = new Node(2);
        root.right = new Node(3);
        root.left.left = new Node(4);
        root.left.right = new Node(5);
        root.right.left = new Node(6);
        root.right.right = new Node(7);
        root.right.left.right = new Node(8);
        root.right.right.right = new Node(9);
        System.out.println("Vertical Order traversal is");
        getVerticalOrder(root);
    }

}
