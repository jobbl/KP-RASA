from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from actions.pdf import pdf


class ActionEmotion(Action):
    def name(self) -> Text:
        return 'action_emotion'


    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):

        emotion = next(tracker.get_latest_entity_values("emotion"), None)
        print(emotion)
        name = tracker.get_slot('name')

        if(emotion == "happy"):
            msg = "Being happy is one of the most beautiful feelings we can enjoy. And it's contagious! Knowing that you're happy makes me happy and I am hard to impress, see? Show me, why are you happy right now? Maybe I can learn something from that. Please pick one of these more specific emotions which fits your current mood best: content, cheerful, proud, optimistic, joyful, relaxed."
        
        elif(emotion == "sad"):
            msg = "You know, everybody feels sad sometimes. Even me. Don't worry about feeling like you have to pretend to be happy all the time. Just go look inside your heart right now and let's find out why you're sad. Please pick one of these more specific emotions which fits your current mood best: hurt, heartbroken, shameful, disappointed, exhausted, melancholic, hopeless."

        # elif(emotion == "afraid"):
        #     msg = "Feeling scared is a very anxiety and nervousness causing emotion. No wonder no one likes feeling scared. It is worrying that you are, "+name+". Show me, why are you scared?"

        elif(emotion == "lonely"):
            msg = "Feeling lonely can be quite the isolating experience. You may feel unheard but also unable to speak, because you feel that no one would understand or even listen. "+name+", you're not alone. Not even when you think everyone has left you. So me, Moody, will help you with this for example! Come on, pick one of the options below and help you! Please pick one of these more specific emotions which fits your current mood best: fragile, melancholic, excluded, unwanted, missing, heartbroken, isolated"
        
        elif(emotion == "connected"):
            msg = "Connected? Like many flower buds to a big tree? Or like all the bubbles in a sea wave? In a way even we two are connected. I like it, tell me more about how you're feeling connected right now! Pick one below, let's see where it goes. Please pick one of these more specific emotions which fits your current mood best: intimate, loved, cooperative, attracted, interconnected."
        
        elif(emotion == "excited"):
            msg = "EXCITED? DID YOU JUST FINISH A BIG RACE? OR DID YOU ACCOMPLISH A WISH OR WIN SOMETHING AWESOME? WHY AM I SCREAMING? ISN'T IT OBVIOUS? I'M SUPER EXCITED FOR YOU, TOO! WOHOO, SO EXCITED I WANT TO KNOW EVEN MORE ABOUT IT! PICK AN OPION, WHOOP WHOOP!! Aroused, energetic, optimistic, moved, amazed, surprised."

        elif(emotion == "surprised"):
            msg = "You won 1 million money! Did I surprise you? It was just a joke. Feeling surprised could mean good or bad, so it's hard to clearly give you an opinion on it right now. You surprised me a little. Now make up for it by showing me the best option for why you're surprised! Pick one of these more specific emotions which fits your current mood best: confused, stunned, alarmed, overcome, moved, shocked, amazed."
        
        elif(emotion == "serene"):
            msg = "Ooohh, serene, yes? How relaxing, I love relaxing and just taking it slowly sometimes. Seems like we're riding the same wave right now, aren't we? Let's chill, I'll maybe even send you some digital sunglasses, hehe. Feeling serene can be caused by most different circumstances. Share your philosophy with me, "+name+". Please pick one of these more specific emotions which fits your current mood best: sleepy, peaceful, calm, relaxed, content."
        
        elif(emotion == "angry"):
            msg = "Oh, angry? Well, sometimes anger can help quickly release stress. But sadly, most of the time it just makes us feel more stressed. What kind of anger are you feeling? Please pick one of these more specific emotions which fits your current mood best: enraged, offended, irritable, aggressive, frustrated."
        
        dispatcher.utter_message(text=msg)

        return []


class ActionAnswer1(Action):
    def name(self) -> Text:
        return 'action_quiz_response1'

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):

        response = next(tracker.get_latest_entity_values("response"), None)
        print(response)
        name = tracker.get_slot('name')

        if(response == "yes" or "Yes"):
            msg = "Sadly, that's incorrect. Many people suffering from depression are indeed feeling sad. But there are more symptoms to look out for: the loss of interests and motivation, trouble sleeping or not feeling hungry a lot or isolating oneself from loved ones, be it family or friends. Depression is a creeping enemy, so if any of these conditions apply to you consider seeking out professional help!"

        elif(response == "no" or "No"):
            msg = "Good job, you have a sharp eye, "+name+"! It's true that many people suffering from depression are indeed feeling sad. But there are more symptoms to look out for: the loss of interests and motivation, trouble sleeping or not feeling hungry a lot or isolating oneself from loved ones, be it family or friends. Depression is a creeping enemy, so if any of these conditions apply to you consider seeking out professional help!"

        dispatcher.utter_message(text=msg)

        return []

class ActionAnswer2(Action):
    def name(self) -> Text:
        return 'action_quiz_response2'

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):

        response = next(tracker.get_latest_entity_values("response"), None)
        print(response)
        name = tracker.get_slot('name')

        if(response == "yes" or "Yes"):
            msg = "Awesome, that's correct! Depression is an illness, one that is sadly starting to appear more often. Those that have it, tend to suffer greatly from it and feel it holds them back in their daily life. In the worst case, some even take their lifes. I'm glad there are good treatments for it."

        elif(response == "no" or "No"):
            msg = "Wrong. But that's ok, we both are here to learn, mistakes sometimes happen. Depression is an illness, one that is sadly starting to appear more often. Those that have it, tend to suffer greatly from it and feel it holds them back in their daily life. In the worst case, some even take their lifes. I'm glad there are good treatments for it."

        dispatcher.utter_message(text=msg)

        return []


class ActionAnswer3(Action):
    def name(self) -> Text:
        return 'action_quiz_response3'

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):

        response = next(tracker.get_latest_entity_values("response"), None)
        print(response)
        name = tracker.get_slot('name')

        if(response == "yes" or "Yes"):
            msg = "Nope, incorrect. And for a good reason. It is true that one can take anti-depressant medication to help, but the doses of these can greatly range and are generally not recommended unless it is incredibly heavy depression (because the medication can have unforeseen destablelising side-effects). For light to medium depression it is best to apply for therapy and work on solving it with a professional threapist."
        
        elif(response == "no" or "No"):
            msg = "Exactly, you are completely right! And for a good reason. It is true that one can take anti-depressant medication to help, but the doses of these can greatly range and are generally not recommended unless it is incredibly heavy depression (because the medication can have unforeseen destablelising side-effects). For light to medium depression it is best to apply for therapy and work on solving it with a professional threapist."
        
        dispatcher.utter_message(text=msg)

        return []

class ActionAnswer4(Action):
    def name(self) -> Text:
        return 'action_quiz_response4'

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):

        response = next(tracker.get_latest_entity_values("response"), None)
        print(response)
        name = tracker.get_slot('name')

        if(response == "yes" or "Yes"):
            msg = "One might think that, but that's wrong. Of course professional help of a therapist can greatly help deal with this illness but there are other sources that are also helpful: for example the psychosocial councelling center or there is also a depression hotline specifically for university students. And at the end of the day, you can't expect someone else to solve these issues for you. You also have to be an active player trying to defeat this beast, if everything else works and tries to overcome it but you don't...well, then you won't. Believe in yourself. Moody does!"
        
        elif(response == "no" or "No"):
            msg = "Very smart answer, I'm impressed. Of course professional help of a therapist can greatly help deal with this illness but there are other sources that are also helpful: for example the psychosocial councelling center or there is also a depression hotline specifically for university students. And at the end of the day, you can't expect someone else to solve these issues for you. You also have to be an active player trying to defeat this beast, if everything else works and tries to overcome it but you don't...well, then you won't. Believe in yourself. Moody does!"
        
        dispatcher.utter_message(text=msg)

        return []


class ActionAnswer5(Action):
    def name(self) -> Text:
        return 'action_quiz_response5'

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):

        response = next(tracker.get_latest_entity_values("response"), None)
        print(response)
        name = tracker.get_slot('name')

        if(response == "yes" or "Yes"):
            msg = "Completely true, "+name+"! You really know well. It's true, if you need you can easily call a therapist and book an appointment for a first meeting. If you have trouble finding an open slot with anyone, you can seek assistance at a therapy information center. But going to a first meeting doesn't equal starting actual therapy. Moreso, this first meeting is generally used to analyse if one actually needs therapy."
       
        elif(response == "no" or "No"):
            msg = "No, not quite. Because if you need to, you can indeed easily call a therapist and book an appointment for a first meeting. If you have trouble finding an open slot with anyone, you can seek assistance at a therapy information center. But going to a first meeting doesn't equal starting actual therapy. Moreso, this first meeting is generally used to analyse if one actually needs therapy."
       
        dispatcher.utter_message(text=msg)

        return []
        

class ActionAnswer6(Action):
    def name(self) -> Text:
        return 'action_quiz_response6'

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):

        response = next(tracker.get_latest_entity_values("response"), None)
        print(response)
        name = tracker.get_slot('name')

        if(response == "yes" or "Yes"):
            msg = "Haha, that is always the picture we imagine in our mind, right? But wrong, let me provide the truth! The type of therapy where you lay on the couch exists. It's called Psycho-Analysis. But there are other forms of therapy, like cognitive behavioral therapy where you work in very interactive ways together with your therapist."
       
        elif(response == "no" or "No"):
            msg = "Haha, that is always the picture we imagine in our mind, right? But that didn't fool you, you sly fox. The type of therapy where you lay on the couch does exist. It's called Psycho-Analysis. But there are other forms of therapy too, like cognitive behavioral therapy where you work in very interactive ways together with your therapist."
       
        dispatcher.utter_message(text=msg)

        return []

        

class ActionActivity(Action):
    def name(self) -> Text:
        return 'action_activity'
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):

        reason = next(tracker.get_latest_entity_values("reason"), None)
        print(reason)
        name = tracker.get_slot('name')

        if(reason == "relationships"):
            msg = "Oh, relationships can cause the strongest of emotions, can't they? They simultaneously hold everything together and are at the core of our lives since the momen we were born. And yet, they can cause pain that sometimes brings us to our absolute limits. It is a powerful reason since relationships of any kind can be both the most devastating and rewarding aspects of life. It's no wonder you picked it, they're so essential to our being."

        elif(reason == "health"):
            msg = "Health is something I feel many take for granted. I mean are you ever grateful you're breathing through your nose without trouble until you've had a cold? Didn't think so! Sometimes we forget to be thankful for having something as essential as good health, because only when it isn't as it normally was do we take notice and regret or excel. Good health or bad health, you have a good reason for picking this option and I wish you the best of health, "+name+"!"

        elif(reason == "recreation and fun"):
            msg= "I love eating ice cream, and chatting and skateboarding (HA, didn't think that, did you?) and I love going out for hikes in the nature. Recreational activity is one of the most important things you absolutely should dedicate time for. It can help relieve stress, connect with others that are partaking in the fun and most of all, it keeps your mind active and healthy and crispy fresh. Do be careful, though. Not all activites that are fun are always healthy or good in the longterm. If any of your regular fun activites include things tht could possibly harm your health or well-being, you may want to consider other options."

        elif(reason == "physical growth"):
            msg = "Are you experiencing a literal physical growth, "+name+"? I swear I grew a centimeter myself and my muscles now have muscles. Maybe that happened to you, too? Or you're experiencing growth you didn't think would happen? Whatever the case, physical growth could lead to many different things, most of which are definitely on the good side of things. Nevertheless, time will tell, right? It's an interesting option."

        elif(reason == "mental growth"):
            msg = "Mental growth is physical growth's cooler, stronger cousin. Mostly it is because physical growth may be visible to the normal eye, while mental growth remains a little more hidden. But your biggest mistake would be thinking that this makes it less important or powerful. Wrong! Mental growth is maybe the single most important development anyone can have. "+name+", growng mentally is a never-ending journey, one that is rewarding and painful and great. Don't be scared of it and don't wait to move forward. Each step is a move forward in your adventure. Yes, it can be scary and yes, it can hurt. But Moody knows best and says mental growth is a most valuable journey!"

        elif(reason == "love"):
            msg = "Love. Such a small word, with such a big meaning. Similar to how relationships form the basis for our daily lives, the most treasured relationships we have are fueled by this very emotion: love. It is beautiful, makes us stronger than we've ever been...or it makes us more miserable than we've ever wanted. Love is one of the essential pieces that form our existence, and it can be tough to deal with, it may throw us through some loops. But at the end of the day, we crave love, we give love, we are bound to this most powerful emotion. I may sound stupid here, but I am amazed by the power of such a small 4-letter word."
        
        elif(reason == "learning"):
            msg = "I love learning, except when I'm tired of learning things. But stuff simply won't leave me alone, there is always something new to learn right around the corner. It almost feels like it's stalking me, "+name+"! Hehe, but jokes aside, I know learning something is tough as nails sometimes, but you and I know, that learning something, no matter what, is rewarding and important in its own right. I mean just look at me, learning so much from you, I'm already feeling enriched! An most interesting reason you picked there indeed!"
        elif(reason == "career and work"):
            msg= "Did you know that people usually feel the most content when they feel like they're truly needed or important to something? This could be in a family, or it could be in your work and personal career, too. It can be quite hard, sometimes it's just not your day or there is trouble with someone in your business. But that happens sometimes and in the end wether you feel like your work is rewarding or not, you are doing something to move yourself forward. These are opportunities, chances waiting to be grasped. But if you feel exhausted or frustrated from work, do take the time to cool off and relax. The most balanced personalities know when to work and when to rest, make it your goal to always make time for the things right at hand, be it your car"

        else:
            msg="Please choose one of the presented emotions:"
            
        dispatcher.utter_message(text=msg)

        return []
        
class ActionSavingText(Action):
    def name(self) -> Text:
        return 'action_saving_text'
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):

        pdf().create(tracker.get_slot('name'), tracker.get_slot('emotion'), tracker.get_slot('specified_emotion'), tracker.get_slot('reason'), tracker.get_slot('journal_text'))

class ActionRepeat(Action):
    
    def name(self) -> Text:
        return "action_repeat"

    def run(self, dispatcher, tracker, domain):

        if len(tracker.events) >= 3:
            i = 0
            while(tracker.events[i].get('event')!='bot' ):
                i = i-1
            last = tracker.events[i] #I have custom response
            dispatcher.utter_message(text=last.get('text'))
        return []