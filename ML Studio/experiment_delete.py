'''
job > experiment 삭제
'''
# 파이프라인 실행 결과 or MLflow 결과로 실험 생성
# 삭제 버튼 없음, 명령어 통해서만 삭제 가능

from azureml.core import Workspace, Experiment

aml_workspace = Workspace.from_config()
experiment_id = Experiment(aml_workspace, '<experiment_name>').id

Experiment.delete(aml_workspace, experiment_id)
