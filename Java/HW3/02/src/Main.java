class Student {
    private String name;
    private String sid;
    private int score;

    public Student() {
    }
    public Student(String name) {
        this.name = name;
    }
    public Student(String name, String sid) {
        this.name = name;
        this.sid = sid;
    }
    public Student(String name, String sid, int score) {
        this.name = name;
        this.sid = sid;
        this.score = score;
    }

    public void setName(String name) {
        this.name = name;
    }
    public void setSid(String sid) {
        this.sid = sid;
    }
    public void setScore(int score) {
        this.score = score;
    }
    public String getName() {
        return name;
    }
    public String getSid() {
        return sid;
    }
    public int getScore() {
        return score;
    }

    public void display(int index) {
        System.out.printf("Student "+index+":\n"+"Name: "+name+"\n"+"ID: "+sid+"\n"+"Score: "+score+"\n");
    }
}

class GradeBook {
    private Student[] records;
    private int totalScore;
    private double averageScore;

    // 函數
    public GradeBook(int size) {
        records = new Student[size];
        totalScore = 0;
        averageScore = 0;
    }

    //新曾
    public void addRecord(Student student, int index) {
        records[index] = student;
        totalScore += student.getScore();
        updateAverage();
    }

    //顯示
    public void displayRecords() {
        for (int i = 0; i < records.length; i++) {
            records[i].display(i+1);
            System.out.println("===============\n");
        }
        System.out.println("Total Score: " + totalScore);
        System.out.printf("Average Score: %.2f\n", averageScore);
    }

    private void updateAverage() {
        averageScore = (double) totalScore / records.length;
    }
}

public class Main {
    public static void main(String[] args) {

        Student[] students = new Student[]{
                new Student("Alice", "A123456", 85),
                new Student("Bob"),
                new Student("Charlie", "C345678"),
                new Student(),
                new Student("Eva", "E567890", 88)
        };
        students[1].setSid("B234567");
        students[1].setScore(92);

        students[2].setScore(78);

        students[3].setName("David");
        students[3].setSid("D456789");
        students[3].setScore(95);

        int numStudents = students.length;
        GradeBook gradeBook = new GradeBook(numStudents);

        for (int i = 0; i < numStudents; i++) {
            gradeBook.addRecord(students[i], i);
        }

        System.out.println("Students Information:\n");
        gradeBook.displayRecords();
    }
}
