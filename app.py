import gradio as gr

# Manual Quick Sort implementation
def quick_sort(arr, snapshots):
    # Base case: if list is empty or has one item, it is sorted
    if len(arr) <= 1:
        return arr
    
    # Selecting the last element as the pivot
    pivot = arr[-1]
    low = []
    high = []
    
    # Partitioning logic: comparing each item to the pivot
    for i in range(len(arr) - 1):
        if arr[i][1] > pivot[1]: # Sorting by highest crowd count first
            high.append(arr[i])
        else:
            low.append(arr[i])
            
        # Record the state of the list for the visual simulation
        snapshots.append(list(high) + [pivot] + list(low))
        
    # Recursive calls to sort the sub-lists
    return quick_sort(high, snapshots) + [pivot] + quick_sort(low, snapshots)

def run_simulation(input_text):
    try:
        # Parse input string into a structured list
        stops = []
        for item in input_text.split(";"):
            name, count = item.split(",")
            stops.append([name.strip(), int(count.strip())])
        
        # Check if list is empty
        if not stops:
            return "Input is empty. Please provide stop data."
            
        # Initialize snapshots with the starting state
        snapshots = [list(stops)]
        final_sorted = quick_sort(stops, snapshots)
        
        # Build the simulation output string
        output = "### Algorithm Steps\n"
        for i, step in enumerate(snapshots):
            output += f"**Step {i+1}:** {step}\n\n"
            
        # Highlight the final decision
        output += "---\n"
        output += f"### Priority Result\n"
        output += f"The extra shuttle should be sent to: **{final_sorted[0][0]}**"
        return output

    except Exception:
        # Return a helpful error message if format is incorrect
        return "Error: Please use the correct format (e.g., Stop A, 10; Stop B, 20)"

# Defining a cleaner, more professional UI layout
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# Campus Shuttle Crowd Ranking System")
    gr.Markdown("This application uses the Quick Sort algorithm to rank shuttle stops by passenger volume.")
    
    with gr.Row():
        # Input column
        with gr.Column():
            input_data = gr.Textbox(
                label="Shuttle Stop Data", 
                placeholder="Enter as: Stop Name, Count; Stop Name, Count",
                lines=3
            )
            submit_btn = gr.Button("Analyze and Sort", variant="primary")
            
        # Output column
        with gr.Column():
            output_display = gr.Markdown("The simulation results will appear here.")
    
    # Connecting the button to the logic
    submit_btn.click(fn=run_simulation, inputs=input_data, outputs=output_display)

demo.launch()
