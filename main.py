from pyscript import document

def candidate_checker(e):
    club_members = [
                    'anthea alavado',
                    'aria bonsol',
                    'gabrielle ibarra',
                    'yijin jeong',
                    'lexi joaquin',
                    'yoninah-dishan lim',
                    'shimeia sanchez',
                    'jadenne saquido',
                    'jillianne singh',
                    'encarna torrejon'
                ]
    
    f_name = document.getElementById('first_name').value.strip()
    l_name = document.getElementById('last_name').value.strip()
    candidate = f_name + ' ' + l_name
    
    member_checker = candidate.lower() in club_members

    messages = (
                f'Sorry, {candidate}. Your name is not on the list.',
                f'Congratulations, {candidate}! You are now a part of Luminara Dance Club!'
            )

    document.getElementById('result').innerHTML = messages[member_checker]
