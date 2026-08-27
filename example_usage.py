from client import AutonomousAgentEvalTrajectoryAnalyzerClient

def main():
    client = AutonomousAgentEvalTrajectoryAnalyzerClient()
    res = client.evaluate_agent_execution_trajectory('run_swe_bench_patch_verifier_42', 30)
    print('Agent Eval Audit: ' + res['eval_audit_id'] + ' | Target: ' + res['target_agent_run'])
    print('Steps: ' + str(res['steps_evaluated_count']) + ' | Tool Success Rate: ' + str(res['tool_call_success_rate_pct']) + '%')
    print('Hallucination Index: ' + str(res['hallucination_index_score']) + ' (Loop Risk: ' + str(res['infinite_loop_risk_detected']) + ')')
    print('Dashboard URL: ' + res['eval_dashboard_analytics_url'])

if __name__ == '__main__':
    main()
