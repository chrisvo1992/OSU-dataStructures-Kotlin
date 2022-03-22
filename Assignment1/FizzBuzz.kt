class FizzBuzz{
    fun fizzBuzz(arr:List<Int>): MutableList<String> {
        var output:MutableList<String> = arrayListOf()

        for(value in arr){
            if(value % 3 == 0 && value % 5 == 0){
                output.add("fizzbuzz")
            } else if (value % 5 ==0){
                output.add("buzz")
            } else if (value % 3 == 0){
                output.add("fizz")
            } else{
                output.add(value.toString())
            }
        }
    return output
    }
}
