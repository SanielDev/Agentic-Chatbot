import streamlit as st 
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMs.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit
def load_langgraph_agenticai_app():
    """
    
    Loads and runs the Langgraph AgenticAI application using Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph on the selected use case, and displays the output while
    implementing exception handling for robustness.
    
    """

    # Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()  # class in the loadui.py file (sidebar gets loaded here)

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return 
    
    user_message = st.chat_input("Enter your message:")

    if user_message:
        try:
            # Configure LLM
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error: LLM model could not be initialized.")
                return 
            
            # Initialize and set up the graph based on the use case
            usecase = user_input.get("selected_usecase")

            if not usecase:
                st.error("Error: usecase not selected.")
                return 
            
            # Graph Builder
            graph_builder = GraphBuilder(model)
            try:
                graph=graph_builder.setup_graph(usecase)
                # setup_graph is based on a specific use case which
                # determines which function to call in graph_builder.py
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph set up failed- {e}")
                return 

        except Exception as e:
            st.error(f"Error: Graph set up failed- {e}")
            return
