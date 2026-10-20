from pyscript import document

def candidate_checker(e):
    club_members = ['anthea alavado', 'aria bonsol', 'gabrielle ibarra', 'yijin jeong', 'lexi joaquin', 'yoninah-dishan lim', 'shimeia sanchez', 'jadenne saquido', 'jillianne singh', 'encarna torrejon']
    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f_name + '' + l_name
    member_checker = candidate.lower() in club_members

    messages = (f'Sorry {candidate}, your name is not on the list',
                f'Congratulations, {candidate}! You are now part of Luminara')

    document.getElementById('result').innerHTML=messages[member_checker]
