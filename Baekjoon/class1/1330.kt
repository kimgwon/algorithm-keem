fun main() {
    val input = System.`in`.bufferedReader()
    val (A, B) = input.readLine().split(" ").map { it.toInt() }
    val result = A-B

    if (result>0) {
        print(">")
    } else if (result<0) {
        print("<")
    } else {
        print("==")
    }
}