// fun main() = with(System.`in`.bufferedReader()){
//     while (true){
//         val input = readLine()
//         if (input.isNullOrEmpty()) break
//         val (A, B) = input.split(" ").map{ it.toInt() }
//         if (A==0 && B==0) break
//         println(A+B)
//     }
// }

// scope 함수를 적용해보자
fun main() = with(System.`in`.bufferedReader()) {
    var input: String?
    while(readLine().also {input = it}.isNullOrEmpty().not()) {
        val (A, B) = input!!.split(" ").map{ it.toInt() }
        println(A+B)
    }
}