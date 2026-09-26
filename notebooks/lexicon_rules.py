# ============================================================
# lexicon_rules.py  —  frozen lexicon 
#   from lexicon_rules import predict_all
#   predict_all(text) -> {"lexicon_1A":0/1, "lexicon_1B":0/1, "lexicon_2":0/1}
# ============================================================
import re
import pandas as pd

# ---- 1A: male in-group + harm ----
ingroup_terms = ["men","man","male","males","boys","boy","fathers","father","dads","dad",
    "husbands","husband","sons","son","young men","white men","western men","brothers",
    "gentlemen","guys","male experience","men's issues","mens issues","men's rights","mens rights",
    "we","we're","we are"]   # first-person plural in-group (manosphere "we vs them")

harm_terms = ["under attack","attacked","attacking","attack","targeted","oppressed","silenced",
    "censored","suppressed","ignored","abandoned","mocked","ridiculed","demonized","demonised",
    "vilified","hated","blamed","punished","discriminated","excluded","marginalized","marginalised",
    "disadvantaged","exploited","used","abused","destroyed","ruined","emasculated","cancelled",
    "canceled","fired","blacklisted","disposable","screwed","biased","rigged","stacked against",
    "unfair","double standard","double standards","no accountability","get away with",
    "false accusation","false accusations","false allegation","false allegations","falsely accused",
    "lied about","no rights","no voice","no respect","nothing to lose","nothing left","no future",
    "get nothing","gets nothing","lose everything","second class","treated like slaves",
    "lose the house","lose your house","take your house","lose the kids","lose your kids",
    "take your kids","lose custody","child support","alimony","take all your money",
    "financially ruined","bankrupted","forced to","expected to","have to pay","have to provide",
    "have to protect","have to sacrifice","die for nothing","pay for nothing","work for nothing",
    "nobody cares","no one cares","loneliness","suicide","system's against","system is against"]

strong_1a_phrases = ["war on men","attack on men","anti male","anti-male","misandry","misandrist",
    "male hatred","men are under attack","men are being attacked","system is against men",
    "system against men","stacked against men","rigged against men","biased against men",
    "men have no rights","fathers have no rights","men are disposable","men are the real victims",
    "nobody cares about men","no one cares about men","men get blamed","men are blamed",
    "men get punished","men are punished","men get nothing","men lose everything",
    "men are being silenced","men are silenced","men are ignored","men are oppressed",
    "men are discriminated against","male loneliness","male suicide","society hates men",
    "men are guilty until proven innocent","marriage is a bad deal","marriage is obsolete",
    "don't get married","do not get married","never get married","family court is broken",
    "family courts are broken","biased courts","court favours women","court favors women",
    "courts favour women","courts favor women",
    "we are being silenced","we are being attacked","we are the victims"]

relationship_terms = ["marriage","married","marry","divorce","dating","relationship","wife","wives",
    "girlfriend","family court","child support","alimony","custody","prenup"]
relationship_risk_terms = ["bad deal","obsolete","risk","lose everything","take half",
    "financially ruined","bankrupt","false accusation","false allegations","nothing to gain",
    "no benefit","no point"]
double_standard_terms = ["double standard","double standards","men have to","men must",
    "men are expected to","women get away with","women don't have to","women do not have to",
    "different rules"]

# ---- 1B: the "move" ----
blame_terms = ["women are to blame","feminism is to blame","feminists are to blame","women caused this",
    "feminism caused this","feminists caused this","women created this","feminism created this",
    "women destroyed","feminism destroyed","women ruined","feminism ruined","they did this to men",
    "women hate us","women use us","women lie about men","feminists hate men","the system hates men",
    "hold women accountable","zero accountability","scot free","nazi feminism"]
withdrawal_terms = ["go your own way","mgtow","stay single","avoid women","avoid dating","stop dating",
    "stop marrying","don't marry","do not marry","never marry","walk away","keep your money",
    "stop paying","stop working","stop protecting","stop sacrificing","stop supporting",
    "stop hiring women","don't hire women","boycott","go on strike","men on strike"]
retaliation_terms = ["fight back","stand against","stand our ground","rise up","revolt","take back",
    "regain our rights","remove their rights","strip women","stop them from voting","remove the vote",
    "deport","military takeover","military take over","civil war","punish them","make women pay",
    "return to patriarchy","enough is enough"]
offensive_demonise_terms = ["believe all women","false accusation","false accusations",
    "false allegation","false allegations","false rape","falsely accused","fake victim","fake victims",
    "playing the victim","cry rape","weaponize","weaponise","metoo","me too","women lie","feminazi",
    "feminists are hitler","war on men","war against men","nazi feminism","genocide against men",
    "male genocide","gynocide"]
strong_1b_phrases = ["men are fighting back","regain our rights and dignity","if men went on strike",
    "men stop paying taxes","hold women accountable","women created this problem",
    "feminism created this problem","strip women of","stop women from voting","remove their rights",
    "go your own way","fight back","stand our ground","civil war","military takeover"]

# ---- 2: conspiratorial framing ----
actor_terms = ["the state","mainstream media","the media","elites","the elites","oligarchs",
    "globalists","united nations","wef","cia","splc","bankers","the fed","central bank","feminism",
    "feminists","sisterhood","powers that be","the matrix","satanic","new world order","deep state",
    "illuminati","freemasons","the government","left wing","left-wing","liberals","democrats","ngos",
    "planned parenthood"]
mechanism_terms = ["by design","designed to","planned to","a plan to","part of the plan",
    "hidden agenda","the agenda","social engineering","engineered","deliberately","intentionally",
    "covertly","in the shadows","behind the scenes","cover up","covering up","covered up","conceal",
    "concealing","hide the truth","hiding the truth","funded","funding","paid to",
    "controlled opposition","gatekeepers","indoctrinate","indoctrinated","indoctrination","subvert",
    "subverted","orchestrated","manufactured","trying to destroy","trying to suppress"]
strong_2_phrases = ["by design","it was all a plan","part of the plan","social engineering",
    "in the shadows","behind the scenes","cover up","covering up","covered up","hidden agenda",
    "powers that be","the matrix","system is satanic","controlled opposition","gatekeepers",
    "systematically destroying","funding feminism"]

# ============================================================
# EXPANSION
# ============================================================
harm_terms += ["subjected to","subject to","prey","predatory","enslaved","expendable","deceived",
    "lied to","sacrificed","taken for granted","set up to fail","thrown under the bus"]
strong_1a_phrases += ["men are prey","men are the prey","men are expendable",
    "men are treated like slaves","men are treated as slaves","men are second class citizens",
    "men are being lied to","men have been lied to","men are set up to fail"]
relationship_risk_terms += ["biased court","biased courts","lose custody","lost custody","silver bullet"]
moral_inversion_terms = ["men are the real victims","men are the true victims","we are the noble gender",
    "men are the noble gender","can't blame men","cannot blame men","can not blame men","no wonder men",
    "what do you expect men to do","women deserve no sympathy","they deserve no sympathy",
    "not our problem","let them suffer","let women suffer","let them fend for themselves",
    "women can fend for themselves","deserve what they get","reap what they sow","let it burn",
    "collapse soon enough"]
mechanism_terms += ["propaganda","push the narrative","pushes the narrative","pushing the narrative",
    "programmed","programming","conditioned","conditioning","scheme","coordinated","coordination",
    "collude","colluded","collusion","set up to","created to","meant to","the goal is",
    "the purpose is","suppress the evidence","suppressing evidence","hide the evidence",
    "hiding evidence","hide the statistics","hiding statistics"]

# ============================================================
# MATCHING HELPERS
# ============================================================
def normalize(text):
    if pd.isna(text): return ""
    t = str(text).lower().replace("’","'").replace("‘","'")
    t = re.sub(r"https?://\S+|www\.\S+", " ", t)
    t = re.sub(r"@\w+", " ", t)
    t = re.sub(r"[^a-z0-9':]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()

def _compile(terms):
    return re.compile(r"(?<!\w)(?:" + "|".join(re.escape(normalize(x)) for x in terms) + r")(?!\w)")

PAT = {name: _compile(terms) for name, terms in dict(
    ingroup=ingroup_terms, harm=harm_terms, s1a=strong_1a_phrases,
    relctx=relationship_terms, relrisk=relationship_risk_terms, ds=double_standard_terms,
    blame=blame_terms, withdrawal=withdrawal_terms, retal=retaliation_terms,
    offdem=offensive_demonise_terms, s1b=strong_1b_phrases, moral_inv=moral_inversion_terms,
    actor=actor_terms, mech=mechanism_terms, s2=strong_2_phrases,
).items()}

THEY_ACTION = re.compile(
    r"\bthey\b.{0,150}\b(by design|the plan|the agenda|engineered|social engineering|"
    r"depopulat|the goal is|created to|funded feminism|cover up|brainwash|indoctrinat)\b")

def has(name, n): return bool(PAT[name].search(n))

def near(a, b, n, max_chars=270):
    xa = [m.start() for m in PAT[a].finditer(n)]
    xb = [m.start() for m in PAT[b].finditer(n)]
    return any(abs(i - j) <= max_chars for i in xa for j in xb)

def is_chapter_list(n):
    return len(re.findall(r"\b\d{1,2}:\d{2}\b", n)) >= 5

# ============================================================
# PREDICTORS
# ============================================================
def predict_1a(n):
    if is_chapter_list(n): return 0
    return int(has("s1a", n)
        or (has("ingroup", n) and has("harm", n))
        or (has("relctx", n) and has("relrisk", n))
        or has("ds", n))

def predict_1b(n):
    if is_chapter_list(n): return 0
    move = (has("blame", n) or has("withdrawal", n) or has("retal", n)
            or has("offdem", n) or has("moral_inv", n))
    return int(has("s1b", n) or (predict_1a(n) == 1 and move))

def predict_2(n):
    if is_chapter_list(n): return 0
    return int(has("s2", n) or near("actor", "mech", n) or bool(THEY_ACTION.search(n)))

def predict_all(text):
    n = normalize(text)
    p1b = predict_1b(n)
    p1a = max(predict_1a(n), p1b)
    return {"lexicon_1A": p1a, "lexicon_1B": p1b, "lexicon_2": predict_2(n)}