import java.util.PriorityQueue;
import java.util.Queue;

public class mergeKLists {
    public static class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    // Priority Queue -> Time complexity: O（N log（k）） Space complexity:  O（k）
    public static ListNode mergeKLists(ListNode[] lists){
        Queue<ListNode> queue = new PriorityQueue<>((a,b)-> a.val - b.val);

        // create a min-heap and insert the all element from lists
        for(ListNode list:lists){
            if(list != null)
                queue.add(list);
        }

        ListNode dummy = new ListNode(0);
        ListNode current = dummy;
        while(!queue.isEmpty()){
            ListNode temp = queue.poll();
            dummy.next= temp;
            dummy = dummy.next;
            if(temp.next != null){
                queue.add(temp.next);
            }
        }
        dummy.next = null;
        return current.next;

    }
    /**
     *
     class Solution {
     public ListNode mergeKLists(ListNode[] lists) {
     PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        for(ListNode head:lists){
            while(head != null){
            minHeap.add(head.val);
            head = head.next;
        }
     }

     ListNode dummy = new ListNode(-1);
     ListNode head = dummy;

     while(!minHeap.isEmpty()) {
            head.next = new ListNode(minHeap.remove());
             head = head.next;
     }
            return dummy.next;
     }
     }
     */


    /**brute-force
    public static ListNode mergeKLists(ListNode[] lists) {
        List<Integer> arrayList = new ArrayList<Integer>();

        for (ListNode list : lists) {
            while (list != null) {
                arrayList.add(list.val);
                list = list.next;
            }
        }

        Collections.sort(arrayList);

        ListNode head = new ListNode(0);
        ListNode current = head;
        for (int i : arrayList) {
            ListNode temp = new ListNode(i);
            current.next = temp;
            current = current.next;
        }
        current.next = null;
        return head.next;
    }
     */

    public static void printList(ListNode head) {
        while (head != null) {
            System.out.print(head.val + " ");
            head = head.next;
        }
    }

    public static void main(String[] args) {
        ListNode[] list = new ListNode[3];
        list[0] = new ListNode(1);
        list[0].next = new ListNode(4);
        list[0].next.next = new ListNode(5);

        list[1] = new ListNode(1);
        list[1].next = new ListNode(3);
        list[1].next.next = new ListNode(4);

        list[2] = new ListNode(2);
        list[2].next = new ListNode(6);

        ListNode head = mergeKLists(list);
        printList(head);


    }
}
