from langgraph.graph import Graph, StateGraph
from typing import TypedDict, List, Dict, Any
from research_agent import gather_data
from answer_drafter import draft_answer

# Try to use the appropriate graph class based on what's available
try:
    # Try newer version first
    from langgraph.graph import StateGraph

    GraphClass = StateGraph
except ImportError:
    try:
        # Try alternate import location
        from langgraph.graph import Graph

        GraphClass = Graph
    except ImportError:
        # Simple fallback if langgraph imports fail
        print("Warning: LangGraph imports failed. Using simplified pipeline instead.")


        class SimplifiedGraph:
            def run(self, query: str) -> str:
                """Simplified pipeline that doesn't use langgraph."""
                raw_data = gather_data(query)
                final_answer = draft_answer(raw_data, query)
                return final_answer


        # Create a simplified graph object for Streamlit to use
        graph = SimplifiedGraph()

        # Exit the module import without running further code
        import sys

        sys.exit(0)


# Define the state structure
class State(TypedDict):
    query: str
    raw_data: List[Dict[str, Any]]
    final_answer: str


# Define the node functions
def gather_data_node(state: State) -> Dict:
    """Node function to gather data using the research agent."""
    query = state["query"]
    raw_data = gather_data(query)
    return {"raw_data": raw_data}


def draft_answer_node(state: State) -> Dict:
    """Node function to draft an answer using the data gathered."""
    query = state["query"]
    raw_data = state["raw_data"]
    final_answer = draft_answer(raw_data, query)
    return {"final_answer": final_answer}


# Create a graph wrapper class for Streamlit to use
class ResearchGraph:
    def __init__(self):
        self.graph = self._create_graph()

    def _create_graph(self):
        # Initialize the graph
        graph = GraphClass(State)

        # Add nodes to the graph
        graph.add_node("gather_data", gather_data_node)
        graph.add_node("draft_answer", draft_answer_node)

        # Define the edges - the flow from one node to another
        graph.add_edge("gather_data", "draft_answer")

        # Set the entry point
        graph.set_entry_point("gather_data")

        # Compile the graph
        return graph.compile()

    def run(self, query: str) -> str:
        """Method to run the graph with a query - this is what Streamlit will call"""
        # Execute the graph with the initial state
        result = self.graph.invoke({"query": query})
        return result["final_answer"]


# Create a graph instance that Streamlit will import
graph = ResearchGraph()

# Stand-alone execution (for testing without Streamlit)
if __name__ == "__main__":
    # Example of running the pipeline with a query
    query = input("Enter your research query: ")
    final_answer = graph.run(query)
    print("\nFinal Answer:")
    print(final_answer)