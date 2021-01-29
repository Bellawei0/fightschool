# Python3 code for the above approach

# Function to find the
# largest lexicographical
# string with given constraints.
def getLargestString(s, k):

    # Vector containing frequency
    # of each character.
    frequency_array = [0] * 26

    # Assigning frequency to
    for i in range(len(s)):

        frequency_array[ord(s[i]) -
                        ord('a')] += 1

    # Empty string of
    # string class type
    ans = ""

    # Loop to iterate over
    # maximum priority first.
    i = 25
    while i >= 0:

        # If frequency is greater than
        # or equal to k.
        if (frequency_array[i] > k):

            # Temporary variable to
            # operate in-place of k.
            temp = k
            st = chr(i + ord('a'))

            while (temp > 0):

                # concatenating with the
                # resultant string ans.
                ans += st
                print(" debug in ans: ", ans)
                temp -= 1

            frequency_array[i] -= k

            # Handling k case by adjusting
            # with just smaller priority
            # element.
            j = i - 1

            while (frequency_array[j] <= 0 and
                    j >= 0):
                j -= 1

            # Condition to verify if index
            # j does have frequency
            # greater than 0;
            if (frequency_array[j] > 0 and
                    j >= 0):

                str1 = chr(j + ord('a'))
                print("debug   : ", str1)
                ans += str1
                frequency_array[j] -= 1

            else:

                # if no such element is found
                # than string can not be
                # processed further.
                break

        # If frequency is greater than 0
        # and less than k.
        elif (frequency_array[i] > 0):

            # Here we don't need to fix K
            # consecutive element criteria.
            temp = frequency_array[i]
            frequency_array[i] -= temp
            st = chr(i + ord('a'))
            print('debug in elif: ', st)
            while (temp > 0):
                ans += st
                temp -= 1

        # Otherwise check for next
        # possible element.
        else:
            i -= 1

    return ans


# Driver code
if __name__ == "__main__":

    S = "xxxxzza"
    k = 3
    print(getLargestString(S, k))

# This code is contributed by Chitranayal
