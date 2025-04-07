package StacksandQueues;

public class Queue {
    private String[] queue;
    private int num_elements = 0;

    public Queue(int capacity){
        queue = new String[capacity];
    }

    public void enqueue(String item){
        // check if queue is full
        if (num_elements == queue.length){
            System.out.println("Queue is full");
            return;
        }

        queue[num_elements] = item;
        num_elements++;
    }

    public String dequeue(){
        // check if queue is empty
        if (num_elements == 0){
            System.out.println("Queue is empty.");
            return "";
        }
        String item = queue[0];
        num_elements--;

        for (int i = 0; i < num_elements; i++){
            queue[i] = queue[i+1];
        }
        return item;
    }
}
