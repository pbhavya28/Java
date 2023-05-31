public class Sum {

    public int add(int a,int b){
        return a+b;
    }
}
class Answer extends Sum{

    public static void main(String[] args) {
        Sum s=new Sum();
        int ans= s.add(4,5);
        System.out.println(ans);
    }
}
