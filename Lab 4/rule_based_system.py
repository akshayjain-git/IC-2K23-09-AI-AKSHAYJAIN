# Simple Rule-Based Expert System

def diagnose(fever, cough, headache):
    if fever and cough:
        return 'Possible Flu'
    elif fever and headache:
        return 'Possible Viral Infection'
    elif cough:
        return 'Possible Common Cold'
    else:
        return 'No matching rule found'

fever = input('Do you have fever? (yes/no): ').lower() == 'yes'
cough = input('Do you have cough? (yes/no): ').lower() == 'yes'
headache = input('Do you have headache? (yes/no): ').lower() == 'yes'

print('Result:', diagnose(fever, cough, headache))
