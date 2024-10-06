// fun main() = with(System.`in`.bufferedReader()){
//     val N = readLine().toInt()
//     val shirts = readLine().split(" ").map { it.toInt() }
//     val (T, P) = readLine().split(" ").map { it.toInt() } 
//     var answer = 0

//     repeat(shirts.size) { i ->
//         answer += if (shirts[i]%T>0) shirts[i]/T+1 else shirts[i]/T
//     }
    
//     println(answer)
//     println("${N/P} ${N%P}")
// }

// 함수형 스타일 적용
fun main() = with(System.`in`.bufferedReader()) {
    val N = readLine().toInt()  // 입력 조건으로 주어진 N 유지
    val shirts = readLine().split(" ").map { it.toInt() }
    val (T, P) = readLine().split(" ").map { it.toInt() }
    
    val answer = shirts.sumOf { (it + T - 1) / T }  // 필요한 값 계산

    println(answer)
    println("${N / P} ${N % P}")  // N에 따른 계산 결과 출력
}
