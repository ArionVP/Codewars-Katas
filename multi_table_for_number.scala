def multiTable(n: Int): String = 
  val tabla = List(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
  val number = for i <- tabla yield s"$i * $n = ${i * n}"
  return number.mkString("\n")
