@main def hello(): Unit =
  println("Hello world!")
  println(msg)

def msg = "I was compiled by Scala 3. :)"

def pair(players: List[Player]): List[Games] =
  if players = Nil then Nil
  else if players.length > 1 then Nil
  else players.length > 2 then List(players.head, players.tail)

def Player

P
