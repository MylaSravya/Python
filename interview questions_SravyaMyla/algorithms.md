## 1) Explain what is an algorithm in computing?
An algorithm is a well-defined computational procedure that take some value as input and generate some value as output. In simple words, it’s a sequence of computational steps that converts input into the output.

## 2) Explain what is Quick Sort algorithm?
Quick Sort algorithm has the ability to sort list or queries quickly. It is based on the principle of partition exchange sort or Divide and conquer. This type of algorithm occupies less space, and it segregates the list into three main parts.

* Elements less than the Pivot element
* Pivot element
* Elements greater than the Pivot element

## 3) Explain what is time complexity of Algorithm?
Time complexity of an algorithm indicates the total time needed by the program to run to completion. It is usually expressed by using the big O notation.

## 4) Mention what are the types of Notation used for Time Complexity?
The types of Notations used for Time Complexity includes

* Big Oh: It indicates “fewer than or the same as” <expression>iterations
* Big Omega: It indicates “more than or same as” <expression>iterations
* Big Theta: It indicates “the same as”<expression>iterations
* Little Oh: It indicates “fewer than” <expression>iterations
* Little Omega: It indicates “more than” <expression>iterations

## 5) Explain how binary search works?
In binary search, we compare the key with the item in the middle position of the array. If the key is less than the item searched then it must lie in the lower half of the array, if the key is greater than the item searched than it should be in upper half of the array.

## 6) Explain whether it is possible to use binary search for linked lists?
Since random access is not acceptable in linked list, it is impossible to reach the middle element of O(1) time. Thus, binary search is not possible for linked list.

## 7) Explain what is heap sort?
Heap-sort can be defined as a comparison based sorting algorithm. It divides its input into the unsorted and sorted region, until it shrinks the unsorted region by eliminating the smallest element and moving that to the sorted region.

## 8) Explain what is Skip list?
Skip list the method for data structuring, where it allows the algorithm to search, delete and insert elements in a symbol table or dictionary. In a skip list, each element is represented by a node. The search function returns the content of the value related to key. The insert operation associates a specified key with a new value, while the delete function deletes the specified key.

## 9) Explain what is Space complexity of insertion sort algorithm?
Insertion sort is an in-place sorting algorithm which means that it requires no extra or little. storage. For insertion sort, it requires only single list elements to be stored out-side the initial data, making the space-complexity 0(1).

## 10) Explain what a “Hash Algorithm” is and what are they used for?
“Hash Algorithm” is a hash function that takes a string of any length and decreases it to a unique fixed length string. It is used for password validity, message & data integrity and for many other cryptographic systems.

## 11) Explain how to find whether the linked list has a loop?
To know whether the linked list has a loop, we will take two pointer approach. If we maintain two pointers, and we increase one pointer after processing two nodes and other after processing every node, we are likely to encounter a situation where both the pointer will be pointing to the same node. This will only occur if linked list has a loop.

## 12) Explain how encryption algorithm works?
Encryption is the process of converting plaintext into a secret code format referred as “Ciphertext”. To convert the text, algorithm uses a string of bits referred as “keys” for calculations. The larger the key, the greater the number of potential patterns for creating cipher text. Most encryption algorithm use codes fixed blocks of input that have length about 64 to 128 bits, while some uses stream method.

## 13) List out some of the commonly used cryptographic algorithms?
Some of the commonly used cryptographic algorithms are

* 3-way
* Blowfish
* CAST
* CMEA
* GOST
* DES and Triple DES
* IDEA
* LOKI and so on

## 14) Explain what is the difference between best case scenario and worst case scenario of an algorithm?
* Best case scenario: Best case scenario for an algorithm is explained as the arrangement of data for which the algorithm performs best. For example, we take a binary search, for which the best case scenario would be if the target value is at the very center of the data you are searching. The best case time complexity would be 0 (1)
* Worst case scenario: It is referred for the worst set of input for a given algorithm. For example quicksort, which can perform worst if you select the largest or smallest element of a sublist for the pivot value. It will cause quicksort to degenerate to O (n2).

## 15) Explain what is Radix Sort algorithm?
Radix sort puts the element in order by comparing the digits of the numbers. It is one of the linear sorting algorithms for integers.

## 16) Explain what is a recursive algorithm?
Recursive algorithm is a method of solving a complicated problem by breaking a problem down into smaller and smaller sub-problems until you get the problem small enough that it can be solved easily. Usually, it involves a function calling itself.

## 17) Mention what are the three laws of recursion algorithm?
All recursive algorithm must follow three laws

* It should have a base case
* A recursive algorithm must call itself
* A recursive algorithm must change its state and move towards the base case

## 18) Explain what is bubble sort algorithm?
Bubble sort algorithm is also referred as sinking sort. In this type of sorting, the list to be sorted out compares the pair of adjacent items. If they are organized in the wrong order, it will swap the values and arrange them in the correct order.

## 19) How do Insertion sort, Heapsort, Quicksort, and Merge sort work?
* Insertion sort takes elements of the array sequentially, and maintains a sorted subarray to the left of the current point. It does this by taking an element, finding its correct position in the sorted array, and shifting all following elements by 1, leaving a space for the element to be inserted.

* Heapsort starts by building a max heap. A binary max heap is a nearly complete binary tree in which each parent node is larger or equal to its children. The heap is stored in the same memory in which the original array elements are. Once the heap is formed, it completely replaces the array. After that, we take and remove the first element, restore the heap property, thus reducing the heap size by 1, after which we place the max element at the end of that memory. This is repeated until we empty out the heap, resulting in the smallest element being in the first place, and the following elements being sequentially larger.

* Quicksort is performed by taking the first (leftmost) element of the array as a pivot point. We then compare it to each following element. When we find one that is smaller, we move it to the left. The moving is performed quickly by swapping that element with the first element after the pivot point, and then swapping the pivot point with the element after it. After going through the whole array, we take all points on the left of the pivot and call quicksort on that subarray, and we do the same to all points on the right of the pivot. The recursion is performed until we reach subarrays of 0-1 elements in length.

* Merge sort recursively halves the given array. Once the subarrays reach trivial length, merging begins. Merging takes the smallest element between two adjacent subarrays and repeats that step until all elements are taken, resulting in a sorted subarray. The process is repeated on pairs of adjacent subarrays until we arrive at the starting array, but sorted.

## 20) What are the key advantages of Insertion Sort, Quicksort, Heapsort and Mergesort? Discuss best, average, and worst case time and memory complexity.

* Insertion sort has an average and worst runtime of O(n^2), and a best runtime of O(n). It doesn’t need any extra buffer, so space complexity is O(1). It is efficient at sorting extremely short arrays due to a very low constant factor in its complexity. It is also extremely good at sorting arrays that are already “almost” sorted. A common use is for re-sorting arrays that have had some small updates to their elements.

* The other three algorithms have a best and average runtime complexity of O(n log n). Heapsort and Mergesort maintain that complexity even in worst case scenarios, while Quicksort has worst case performance of O(n^2).

* Quicksort is sensitive to the data provided. Without usage of random pivots, it uses O(n^2) time for sorting a full sorted array. But by swapping random unsorted elements with the first element, and sorting afterwards, the algorithm becomes less sensitive to data would otherwise cause worst-case behavior (e.g. already sorted arrays). Even though it doesn’t have lower complexity than Heapsort or Merge sort, it has a very low constant factor to its execution speed, which generally gives it a speed advantage when working with lots of random data.

* Heapsort has reliable time complexity and doesn’t require any extra buffer space. As a result, it is useful in software that requires reliable speed over optimal average runtime, and/or has limited memory to operate with the data. Thus, systems with real time requirements and memory constraints benefit the most from this algorithm.

* Merge sort has a much smaller constant factor than Heapsort, but requires O(n) buffer space to store intermediate data, which is very expensive. Its main selling point is that it is stable, as compared to Heapsort which isn’t. In addition, its implementation is very parallelizable.
  
## 21) What is the function of a Pivot element?
This is another shallow dive into the basics of algorithms. You can answer by explaining that a pivot element is an element chosen from the array or matrix being worked on to serve as the first element selected by the algorithm to perform calculations.

There are many ways to pick a pivot element. For arrays, pivots can be the last or first element, chosen from the middle, or even randomly selected.  Depending on the algorithm, the way in which the pivot is selected may yield better results.

## 22) 