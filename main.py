from src.orchestration.pydantic_orchestrator import SupplyChainWorkflow

def main():
    workflow = SupplyChainWorkflow()
    print("\nEnterprise GenAI Supply Chain Risk Intelligence Assistant")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("Ask a Supply Chain Question: ").strip()
        if not query:
            print("\nPlease enter a valid question.\n")
            continue
        if query.lower() == "exit":
            print("\nThank you for using the assistant!")
            break
        try:
            result = workflow.execute(query)
            print("\nRetrieved Documents:\n")
            for doc in result.documents:
                print(doc)
            print("\nRisks Identified:")
            if result.risks:
                for risk in result.risks:
                    print(f"- {risk}")
            else:
                print("No risks detected.")
            print("\nRecommendations:")
            if result.recommendations:
                for recommendation in result.recommendations:
                    print(f"- {recommendation}")
            else:
                print("No recommendations generated.")
            print("\nExecutive Investigation Report:\n")
            print(result.report)
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}\n")

if __name__ == "__main__":
    main()