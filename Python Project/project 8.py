import numpy as np

class NumPyAnalyzer:
    def __init__(self):
        self.arr = None

    def _get_int_input(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a number.")
            except EOFError:
                print("\nInput stream closed. Exiting current operation.")
                return None
            except KeyboardInterrupt:
                print("\nOperation cancelled.")
                return None

    def _ensure_array_exists(self):
        if self.arr is None:
            print("\n Please create an array first using option 1!")
            return False
        return True

    def create_array(self):
        print("\n---  Array Creation ---")
        print("Select the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")

        subchoice = self._get_int_input("Enter your choice: ")
        if subchoice is None: return

        try:
            if subchoice == 1:
                size = self._get_int_input("\nEnter the number of elements: ")
                if size is None: return
                
                elements = list(map(int, input(f"Enter {size} elements separated by space: ").split()))
                if len(elements) != size:
                    print(f"Error: Expected {size} elements but received {len(elements)}.")
                    return
                
                self.arr = np.array(elements)
                print("\n 1D Array created successfully:")
                print(self.arr)

            elif subchoice == 2:
                rows = self._get_int_input("\nEnter the number of rows: ")
                cols = self._get_int_input("Enter the number of columns: ")
                if rows is None or cols is None: return

                total = rows * cols
                elements = list(map(int, input(f"Enter {total} elements separated by space: ").split()))
                if len(elements) != total:
                    print(f"Error: Expected {total} elements but received {len(elements)}.")
                    return
                
                self.arr = np.array(elements).reshape(rows, cols)
                print("\n 2D Array created successfully:")
                print(self.arr)
                
                self._2d_array_sub_menu()

            else:
                print("Invalid choice for array type.")
        
        except ValueError:
            print("Invalid input. Please ensure all elements are valid integers.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def _2d_array_sub_menu(self):
        rows, cols = self.arr.shape
        while True:
            print("\n---  2D Indexing/Slicing ---")
            print("1. Indexing (Access single element)")
            print("2. Slicing (Access subarray)")
            print("3. Go Back")

            op = self._get_int_input("Enter your choice: ")
            if op is None: return

            try:
                if op == 1:
                    r = self._get_int_input(f"\nEnter row index (0 to {rows - 1}): ")
                    c = self._get_int_input(f"Enter column index (0 to {cols - 1}): ")
                    if r is None or c is None: continue
                    print("\nIndexed Value:", self.arr[r, c]) 
                    

                elif op == 2:
                    r_slice = input("Enter the row slice (e.g., 0:2, :3, or 1:): ")
                    c_slice = input("Enter the column slice (e.g., 0:2, :3, or 1:): ")
                    
                    row_slice_obj = eval('slice({})'.format(r_slice.replace(':', ',')))
                    col_slice_obj = eval('slice({})'.format(c_slice.replace(':', ',')))
                    
                    print("\nSliced Array:")
                    print(self.arr[row_slice_obj, col_slice_obj])
                    

                elif op == 3:
                    print("\nReturning to main menu...")
                    break
                else:
                    print("Invalid operation! Try again.")
            
            except IndexError:
                print("Index out of bounds! Check your row/column limits.")
            except Exception as e:
                print(f"Invalid slicing input: {e}")


    def perform_math_operations(self):
        print("\n--- Mathematical Operations ---")
        print("Choose a mathematical operation (Element-wise):")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        op = self._get_int_input("Enter your choice: ")
        if op is None: return

        try:
            rows = self._get_int_input("\nEnter the number of rows for both arrays: ")
            cols = self._get_int_input("Enter the number of columns for both arrays: ")
            if rows is None or cols is None: return
            total = rows * cols

            elements1 = list(map(int, input(f"\nEnter the first array elements ({total} elements separated by space): ").split()))
            if len(elements1) != total:
                 print(f"Error: Expected {total} elements for array 1.")
                 return
            arr1 = np.array(elements1).reshape(rows, cols)

            elements2 = list(map(int, input(f"Enter the second array elements ({total} elements separated by space): ").split()))
            if len(elements2) != total:
                 print(f"Error: Expected {total} elements for array 2.")
                 return
            arr2 = np.array(elements2).reshape(rows, cols)

            print("\nOriginal Array 1:")
            print(arr1)
            print("\nOriginal Array 2:")
            print(arr2)

            if op in [1, 2, 3, 4]:
                print("\nResult:")
                if op == 1:
                    print(arr1 + arr2)
                elif op == 2:
                    print(arr1 - arr2)
                elif op == 3:
                    print(arr1 * arr2)
                elif op == 4:
                    result = np.divide(arr1, arr2, out=np.full_like(arr1, np.inf, dtype=float), where=arr2!=0)
                    print(result)
            else:
                print("Invalid mathematical operation!")

        except ValueError:
            print("Invalid input. Please ensure all inputs are valid integers.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def combine_or_split_arrays(self):
        if not self._ensure_array_exists(): return
        
        if self.arr.ndim < 2:
            print("\n Warning: Combination/Splitting works best on 2D arrays.")
        elif self.arr.shape[0] % 2 != 0:
            print("\n Warning: Array has an odd number of rows and cannot be split into 2 equal parts.")
            
        print("\n---  Combine or Split Arrays ---")
        print("Current Array shape:", self.arr.shape)
        print("1. Combine Arrays (Vertical Stack - np.vstack)")
        print("2. Split Array (Vertical Split - np.vsplit into 2 parts)")

        op = self._get_int_input("Enter your choice: ")
        if op is None: return

        if op == 1:
            try:
                shape = self.arr.shape
                total = np.prod(shape)
                print(f"\nEnter the elements of another array to combine ({total} elements separated by space):")
                new_elements = list(map(int, input().split()))
                if len(new_elements) != total:
                     print(f"Error: Expected {total} elements for the second array.")
                     return
                
                arr2 = np.array(new_elements).reshape(shape)

                print("\nOriginal Array 1:")
                print(self.arr)
                print("\nOriginal Array 2:")
                print(arr2)
                
                print("\nCombined Array (Vertical Stack - np.vstack):")
                print(np.vstack((self.arr, arr2))) 
                

            except Exception as e:
                print(f"Error during combination. Check array shapes: {e}")

        elif op == 2:
            try:
                if self.arr.ndim < 2 or self.arr.shape[0] % 2 != 0:
                    print("\nCannot perform vsplit: Array must be 2D and have an even number of rows.")
                    return
                    
                part1, part2 = np.vsplit(self.arr, 2)
                print("\nArray Split (np.vsplit) into 2 parts:")
                print("--- First Part:")
                print(part1)
                print("--- Second Part:")
                print(part2)
                
            except Exception as e:
                print(f"Error during splitting: {e}")

        else:
            print("Invalid option!")

    def search_sort_filter(self):
        if not self._ensure_array_exists(): return
        
        print("\n---  Search, Sort, or Filter Arrays ---")
        print("Original Array:")
        print(self.arr)
        print("1. Search for an Element (np.where)")
        print("2. Sort the Array (np.sort)")
        print("3. Filter Elements Greater than a Value (Boolean Indexing)")

        op = self._get_int_input("Enter your choice: ")
        if op is None: return

        try:
            if op == 1:
                val = self._get_int_input("\nEnter the element to search for: ")
                if val is None: return
                result = np.where(self.arr == val)
                
                if result[0].size > 0:
                    if self.arr.ndim == 1:
                         print(f"\nElement {val} found at indices: {result[0]}")
                    else:
                         print(f"\nElement {val} found at indices (row, col): {list(zip(result[0], result[1]))}")
                else:
                    print(f"\nElement {val} not found in the array.")
                

            elif op == 2:
                print("\nSorted Array (flat sort, reshaped to original dimensions):")
                sorted_arr = np.sort(self.arr, axis=None)
                print(sorted_arr.reshape(self.arr.shape))
                

            elif op == 3:
                threshold = self._get_int_input("\nEnter the threshold value: ")
                if threshold is None: return
                
                filtered_arr = self.arr[self.arr > threshold]
                print(f"\nElements greater than {threshold} (Filtered Array):")
                print(filtered_arr)
                
                
            else:
                print("Invalid option!")

        except Exception as e:
            print(f"An error occurred: {e}")

    def compute_aggregates_stats(self):
        if not self._ensure_array_exists(): return

        print("\n---  Compute Aggregates and Statistics ---")
        print("Original Array:")
        print(self.arr)
        print("Choose an aggregate/statistical operation:")
        print("1. Sum (np.sum)")
        print("2. Mean (np.mean)")
        print("3. Median (np.median)")
        print("4. Standard Deviation (np.std)")
        print("5. Variance (np.var)")

        op = self._get_int_input("Enter your choice: ")
        if op is None: return

        try:
            if op == 1:
                print("\nSum of Array:", np.sum(self.arr))
            elif op == 2:
                print("\nMean of Array:", np.mean(self.arr))
            elif op == 3:
                print("\nMedian of Array:", np.median(self.arr))
            elif op == 4:
                print("\nStandard Deviation of Array:", np.std(self.arr))
            elif op == 5:
                print("\nVariance of Array:", np.var(self.arr))
            else:
                print("Invalid choice!")
        except Exception as e:
            print(f"An error occurred during computation: {e}")

    def run(self):
        while True:
            print("\n====================================")
            print("Welcome to the NumPy Analyzer!")
            print("====================================")
            print(f"Current Array Status: {'None' if self.arr is None else f'{self.arr.shape} Array'}")
            print("Choose an option:")
            print("1. Create/Modify NumPy Array")
            print("2. Perform Mathematical Operations (Element-wise)")
            print("3. Combine or Split Arrays")
            print("4. Search, Sort, or Filter Arrays")
            print("5. Compute Aggregates and Statistics")
            print("6. Exit")

            choice = self._get_int_input("Enter your choice: ")
            if choice is None: continue

            if choice == 1:
                self.create_array()
            elif choice == 2:
                self.perform_math_operations()
            elif choice == 3:
                self.combine_or_split_arrays()
            elif choice == 4:
                self.search_sort_filter()
            elif choice == 5:
                self.compute_aggregates_stats()
            elif choice == 6:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice! Please select an option between 1 and 6.")

if __name__ == "__main__":
    analyzer = NumPyAnalyzer()
    analyzer.run()
