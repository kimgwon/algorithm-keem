// fun main() = with(System.`in`.bufferedReader()) {
//     val N = readLine()
//     val nums = readLine().split(" ").map { it.toInt() }
//     var answer = 0

//     for (num in nums) {
//         if (isPrime(num)) answer++
//     }

//     println(answer)
// }

// fun isPrime(num: Int): Boolean {
//     if (num <= 1) return false
//     for (i in 2..num/2) {
//         if (num % i == 0) return false
//     }
//     return true
// }

// 함수형 스타일 적용
fun main() = with(System.`in`.bufferedReader()) {
    val N = readLine()
    val nums = readLine().split(" ").map { it.toInt() }

    val answer = nums.count { isPrime(it) }  // filter + count로 대체

    println(answer)
}

fun isPrime(num: Int): Boolean {
    if (num <= 1) return false
    return (2..num / 2).none { num % it == 0 }  // none을 사용해 간결하게
}
