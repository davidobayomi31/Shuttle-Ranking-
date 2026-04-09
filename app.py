import gradio as gr

def quick_sort(arr, snapshots, full_list_ref, start_idx):
    # Base case: if the sub-array has 0 or 1 elements, it is already sorted
    if len(arr) <= 1:
        return arr
        
    # Choosing the last element as the pivot for partitioning
    pivot = arr[-1]
    low = []
    high = []
        
    # Divide elements into 'high' (more people) and 'low' (fewer people)
    for i in range(len(arr) - 1):
        if arr[i][1] > pivot[1]: # Higher crowd count = higher priority
            high.append(arr[i])
        else:
            low.append(arr[i])
                    
    # Update the reference list to show the movement in the context of the full list
    current_partition = high + [pivot] + low + arr[i+1:-1]
    full_list_ref[start_idx : start_idx + len(arr)] = current_partition
    
    # Save a copy of the current list state to the snapshots list
    snapshots.append(list(full_list_ref))
            
    # Recursively sort the high (left) side
    sorted_high = quick_sort(high, snapshots, full_list_ref, start_idx)
    
    # Place the pivot in its final sorted position within the reference list
    mid_idx = start_idx + len(high)
    full_list_ref[mid_idx] = pivot
    
    # Recursively sort the low (right) side
    sorted_low = quick_sort(low, snapshots, full_list_ref, mid_idx + 1)
        
    # Return the combined sorted list
    return sorted_high + [pivot] + sorted_low

def run_simulation(input_text):
    try:
        # Convert the raw string input into a list of [Name, Count] pairs
        stops = []
        for item in input_text.split(";"):
            name, count = item.split(",")
            stops.append([name.strip(), int(count.strip())])
                
        if not stops:
            return "Input is empty. Please provide stop data."
                    
        # Initialize the snapshots with the unsorted list
        snapshots = [list(stops)]
        
        # Create a reference list that gets modified during the recursive calls
        full_list_ref = list(stops)
        final_sorted = quick_sort(stops, snapshots, full_list_ref, 0)
                
        # Format the output using Markdown for the Gradio display
        output = "### Algorithm Steps (Full List View)\n"
        output += "This view shows how the algorithm reorders the entire list step-by-step.\n\n"
        
        for i, step in enumerate(snapshots):
            # Create a readable string for each step of the process
            formatted_step = " | ".join([f"{s[0]} ({s[1]})" for s in step])
            output += f"**Step {i+1}:** {formatted_step}\n\n"
                    
        output += "---\n"
        output += f"### Priority Result\n"
        output += f"The extra shuttle should be sent to: **{final_sorted[0][0]}**"
        return output
    except Exception:
        # Basic error handling for malformed input
        return "Error: Please use the correct format (e.g., Stop A, 10; Stop B, 20)"

# Set up the Gradio interface using the Soft theme
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# Campus Shuttle Crowd Ranking System")
    gr.Markdown("Watch the Quick Sort algorithm partition and rank the full list of campus stops.")
        
    with gr.Row():
        with gr.Column():
            # Input textbox for stop data
            input_data = gr.Textbox(
                label="Shuttle Stop Data", 
                placeholder="Enter as: Stop A, 85; Stop B, 12; Stop C, 45",
                lines=3
            )
            submit_btn = gr.Button("Analyze and Sort", variant="primary")
                    
        with gr.Column():
            # Area to display the step-by-step results
            output_display = gr.Markdown("The simulation results will appear here.")
        
        # Link the button to the processing function
        submit_btn.click(fn=run_simulation, inputs=input_data, outputs=output_display)

# Run the app
demo.launch()
