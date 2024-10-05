// fun main() = with(System.`in`.bufferedReader()){
//     val n = readLine().toInt()
//     val input = readLine()
//     var sum = 0
//     repeat(n){
//         sum += input[it].toString().toInt()
//     }
//     println(sum)
// }

// sumOf 사용하자.
fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine()!!.toInt()
    val sum = readLine()!!.sumOf { it.digitToInt() }
    println(sum)
}