// import kotlin.math.*

// fun main() = with(System.`in`.bufferedReader()){
//     while(true){
//         val sides = readLine().split(" ").map{it.toDouble()}
//         if (sides.all{it==0.0}){
//             break
//         }
//         val sorted_sides = sides.sorted()
//         if (sorted_sides[0].pow(2.0) + sorted_sides[1].pow(2) == sorted_sides[2].pow(2))
//             println("right")
//         else 
//             println("wrong")
//     }    
// }

// 가독성 높이기
import kotlin.math.pow

fun main() = with(System.`in`.bufferedReader()) {
    while (true) {
        val sides = readLine().split(" ").map{it.toDouble()}

        if (sides.all { it == 0.0 }) break

        val (a, b, c) = sides.sorted()
        println(if (a.pow(2) + b.pow(2) == c.pow(2)) "right" else "wrong")
    }
}